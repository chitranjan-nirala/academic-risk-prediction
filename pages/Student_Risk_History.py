import streamlit as st
from src.ui.sidebar  import render_sidebar
from src.database.db import PredictionDatabase
from src.ui.styles import load_css

st.set_page_config(
    page_title="Student Risk History",
    page_icon="🕒",
    layout="wide"
)

load_css()

# ===================================
# SIDEBAR - 
# ===================================
render_sidebar()  

# Custom header with consistent styling
st.markdown("""
<div class="history-header-card">
    <div class="history-header-left">
        <div class="history-header-icon">🕒</div>
        <div>
            <div class="history-header-title">Student Risk History</div>
            <div class="history-header-subtitle">Track and analyze student risk predictions over time</div>
        </div>
    </div>
    <div class="history-header-right">
        <div class="history-header-badge">Historical Data</div>
    </div>
</div>
""", unsafe_allow_html=True)

db = PredictionDatabase()
df = db.get_predictions_dataframe()

if df.empty:
    st.markdown("""
    <div class="history-empty-state">
        <div class="empty-state-icon">📭</div>
        <div class="empty-state-title">No Prediction History Available</div>
        <div class="empty-state-text">Generate predictions to start tracking student risk history.</div>
    </div>
    """, unsafe_allow_html=True)
    st.stop()

# ===================================
# FILTERS
# ===================================

st.markdown("""
<div class="history-filters-card">
    <div class="history-filters-header">
        <div class="history-filters-header-left">
            <span class="history-filters-icon">🔍</span>
            <span class="history-filters-title">Filter Records</span>
        </div>
        <div class="history-filters-badge">Refine Results</div>
    </div>
    <div class="history-filters-container">
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    selected_risk = st.selectbox(
        "Risk Level",
        ["All", "High Risk", "Medium Risk", "Low Risk"],
        key="history_risk_filter"
    )

with col2:
    age_filter = st.slider(
        "Minimum Age",
        15,
        30,
        15,
        key="history_age_filter"
    )

st.markdown("</div></div>", unsafe_allow_html=True)

# Apply filters
filtered_df = df.copy()

if selected_risk != "All":
    filtered_df = filtered_df[filtered_df["risk_level"] == selected_risk]

filtered_df = filtered_df[filtered_df["age"] >= age_filter]

st.markdown('<div class="history-divider"></div>', unsafe_allow_html=True)

# ===================================
# RESULTS
# ===================================

# Show record count
st.markdown(f"""
<div class="history-stats-card">
    <div class="history-stats-content">
        <div class="stats-icon">📊</div>
        <div class="stats-text">
            <span class="stats-count">{len(filtered_df)}</span>
            <span class="stats-label">records found</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ===================================
# DATA TABLE
# ===================================

st.markdown("""
<div class="history-table-card">
    <div class="history-table-header">
        <div class="history-table-header-left">
            <span class="history-table-icon">📋</span>
            <span class="history-table-title">Prediction Records</span>
        </div>
        <div class="history-table-badge">Chronological Order</div>
    </div>
    <div class="history-table-container">
""", unsafe_allow_html=True)

# Style the dataframe with risk-based coloring
def color_risk_level(val):
    """Apply color coding to risk levels"""
    if val == "High Risk":
        return 'color: #EF4444; font-weight: 600'
    elif val == "Medium Risk":
        return 'color: #F59E0B; font-weight: 600'
    elif val == "Low Risk":
        return 'color: #10B981; font-weight: 600'
    return ''

def color_risk_probability(val):
    """Apply color coding to risk probability"""
    if isinstance(val, (int, float)):
        if val >= 70:
            return 'color: #EF4444; font-weight: 600'
        elif val >= 40:
            return 'color: #F59E0B; font-weight: 600'
        elif val < 40:
            return 'color: #10B981; font-weight: 600'
    return ''

# Apply styling to dataframe
styled_df = filtered_df.style.map(
    color_risk_level, 
    subset=["risk_level"]
).map(
    color_risk_probability, 
    subset=["risk_probability"]
)

# Format numeric columns
styled_df = styled_df.format({
    "risk_probability": "{:.1f}%",
    "age": "{:.0f}",
    "attendance": "{:.0f}",
    "study_hours": "{:.1f}",
    "previous_grades": "{:.0f}"
})

st.dataframe(
    styled_df,
    use_container_width=True,
    hide_index=True,
    height=500
)

st.markdown("</div></div>", unsafe_allow_html=True)

st.markdown('<div class="history-divider"></div>', unsafe_allow_html=True)

# ===================================
# EXPORT SECTION
# ===================================

st.markdown("""
<div class="history-export-card">
    <div class="history-export-header">
        <div class="history-export-header-left">
            <span class="history-export-icon">⬇️</span>
            <span class="history-export-title">Export Data</span>
        </div>
        <div class="history-export-badge">CSV Format</div>
    </div>
    <div class="history-export-container">
""", unsafe_allow_html=True)

csv = filtered_df.to_csv(index=False)

col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
with col_btn2:
    st.download_button(
        label="📥 Download History as CSV",
        data=csv,
        file_name="prediction_history.csv",
        mime="text/csv",
        use_container_width=True,
        key="history_download_btn"
    )

st.markdown("</div></div>", unsafe_allow_html=True)