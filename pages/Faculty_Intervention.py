import streamlit as st
from src.ui.sidebar  import render_sidebar
from src.database.db import PredictionDatabase
from src.ui.styles import load_css

st.set_page_config(
    page_title="Faculty Intervention",
    page_icon="🎯",
    layout="wide"
)

load_css()

# ===================================
# SIDEBAR - 
# ===================================
render_sidebar()  

# Custom header with consistent styling
st.markdown("""
<div class="intervention-header-card">
    <div class="intervention-header-left">
        <div class="intervention-header-icon">🎯</div>
        <div>
            <div class="intervention-header-title">Faculty Intervention Center</div>
            <div class="intervention-header-subtitle">Track and manage at-risk student interventions</div>
        </div>
    </div>
    <div class="intervention-header-right">
        <div class="intervention-header-badge">Action Required</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ===================================
# DATABASE
# ===================================

db = PredictionDatabase()
df = db.get_high_risk_students()

if df.empty:
    st.markdown("""
    <div class="intervention-empty-state">
        <div class="empty-state-icon">✅</div>
        <div class="empty-state-title">No High-Risk Students</div>
        <div class="empty-state-text">All students are currently on track. Great job!</div>
    </div>
    """, unsafe_allow_html=True)
    st.stop()

# ===================================
# KPI CARDS
# ===================================

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(f"""
    <div class="intervention-metric-card">
        <div class="metric-icon">⚠️</div>
        <div class="metric-value">{len(df)}</div>
        <div class="metric-label">High Risk Students</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="intervention-metric-card">
        <div class="metric-icon">⏳</div>
        <div class="metric-value">{db.get_pending_cases()}</div>
        <div class="metric-label">Pending Cases</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="intervention-metric-card">
        <div class="metric-icon">✅</div>
        <div class="metric-value">{db.get_resolved_cases()}</div>
        <div class="metric-label">Resolved Cases</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="intervention-divider"></div>', unsafe_allow_html=True)

# ===================================
# HIGH RISK TABLE
# ===================================

st.markdown("""
<div class="intervention-table-card">
    <div class="intervention-table-header">
        <div class="intervention-table-header-left">
            <span class="intervention-table-icon">🚨</span>
            <span class="intervention-table-title">Students Requiring Intervention</span>
        </div>
        <div class="intervention-table-badge">High Priority</div>
    </div>
    <div class="intervention-table-container">
""", unsafe_allow_html=True)

# Style the dataframe with risk coloring
def color_risk_level(val):
    """Apply color coding to risk probability"""
    if isinstance(val, (int, float)):
        if val >= 70:
            return 'color: #EF4444; font-weight: 600'
        elif val >= 40:
            return 'color: #F59E0B; font-weight: 600'
    return ''

styled_df = df.style.map(color_risk_level, subset=["risk_probability"])

st.dataframe(
    styled_df,
    use_container_width=True,
    hide_index=True,
    height=400
)

st.markdown("</div></div>", unsafe_allow_html=True)

st.markdown('<div class="intervention-divider"></div>', unsafe_allow_html=True)

# ===================================
# UPDATE INTERVENTION
# ===================================

st.markdown("""
<div class="intervention-form-card">
    <div class="intervention-form-header">
        <div class="intervention-form-header-left">
            <span class="intervention-form-icon">📝</span>
            <span class="intervention-form-title">Intervention Tracking</span>
        </div>
        <div class="intervention-form-badge">Update Status</div>
    </div>
    <div class="intervention-form-container">
""", unsafe_allow_html=True)

student_id = st.selectbox(
    "Select Student ID",
    df["id"].tolist(),
    key="intervention_student"
)

mentor = st.text_input(
    "Assign Mentor",
    placeholder="e.g., Dr. Smith, Prof. Johnson",
    key="intervention_mentor"
)

status = st.selectbox(
    "Status",
    ["Pending", "In Progress", "Resolved"],
    key="intervention_status"
)

col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
with col_btn2:
    if st.button(
        "📌 Update Intervention",
        use_container_width=True,
        key="update_intervention_btn"
    ):
        db.update_intervention(
            student_id,
            status,
            mentor
        )
        st.success("✅ Intervention updated successfully!")
        st.rerun()

st.markdown("</div></div>", unsafe_allow_html=True)