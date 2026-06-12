import streamlit as st
import pandas as pd
import plotly.express as px
from src.ui.sidebar  import render_sidebar
from src.ui.styles import load_css
from src.database.db import PredictionDatabase
from src.components.analytics_engine import AnalyticsEngine
from src.ui.analytics_cards import render_analytics_cards

st.set_page_config(
    page_title="Analytics",
    page_icon="📊",
    layout="wide"
)

load_css()

# ===================================
# LOAD DATA
# ===================================

db = PredictionDatabase()
df = db.get_predictions_dataframe()

# ===================================
# SIDEBAR - 
# ===================================
render_sidebar()  

# Custom header with consistent styling
st.markdown("""
<div class="analytics-header-card">
    <div class="analytics-header-left">
        <div class="analytics-header-icon">📊</div>
        <div>
            <div class="analytics-header-title">Cohort Analytics Dashboard</div>
            <div class="analytics-header-subtitle">Real-time student risk monitoring & insights</div>
        </div>
    </div>
    <div class="analytics-header-right">
        <div class="analytics-header-badge">● Live Data</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ===================================
# EMPTY CHECK
# ===================================

if df.empty:
    st.markdown("""
    <div class="analytics-empty-state">
        <div class="empty-state-icon">📭</div>
        <div class="empty-state-title">No Data Available</div>
        <div class="empty-state-text">No prediction history found. Generate predictions to see analytics.</div>
    </div>
    """, unsafe_allow_html=True)
    st.stop()

# ===================================
# CLEAN DATA
# ===================================

df["timestamp"] = pd.to_datetime(df["timestamp"])

# ===================================
# SUMMARY METRICS
# ===================================

engine = AnalyticsEngine()
summary = engine.generate_summary(df)

render_analytics_cards(summary)

# Custom divider
st.markdown('<div class="analytics-divider"></div>', unsafe_allow_html=True)

# ===================================
# CHARTS
# ===================================

left_col, right_col = st.columns(2)

# ===================================
# RISK DISTRIBUTION
# ===================================

with left_col:
    st.markdown("""
    <div class="chart-minimal-card">
        <div class="chart-minimal-header">
            <span class="chart-minimal-icon">🥧</span>
            <span class="chart-minimal-title">Risk Distribution</span>
            <span class="chart-minimal-badge">Current Cohort</span>
        </div>
        <div class="chart-minimal-container">
    """, unsafe_allow_html=True)
    
    risk_df = pd.DataFrame({
        "Risk Level": [
            "High Risk",
            "Medium Risk",
            "Low Risk"
        ],
        "Count": [
            summary["high_risk"],
            summary["medium_risk"],
            summary["low_risk"]
        ]
    })
    
    # Custom color mapping
    color_map = {
        "High Risk": "#EF4444",
        "Medium Risk": "#F59E0B",
        "Low Risk": "#10B981"
    }
    
    fig1 = px.pie(
        risk_df,
        names="Risk Level",
        values="Count",
        hole=0.55,
        title="",
        color="Risk Level",
        color_discrete_map=color_map
    )
    
    fig1.update_layout(
        template="plotly_dark",
        height=400,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Inter, sans-serif", size=12, color="#D1D5DB"),
        showlegend=True,
        legend=dict(
            bgcolor="rgba(17, 19, 24, 0.8)",
            bordercolor="rgba(99, 102, 241, 0.2)",
            borderwidth=1,
            font=dict(size=11)
        )
    )
    
    fig1.update_traces(
        textposition='outside',
        textinfo='percent+label',
        textfont_size=12,
        marker=dict(line=dict(color='rgba(17, 19, 24, 0.8)', width=2))
    )
    
    st.plotly_chart(
        fig1,
        use_container_width=True,
        config={"displayModeBar": False}
    )
    
    st.markdown("</div></div>", unsafe_allow_html=True)

# ===================================
# RISK TREND
# ===================================

with right_col:
    st.markdown("""
    <div class="chart-minimal-card">
        <div class="chart-minimal-header">
            <span class="chart-minimal-icon">📈</span>
            <span class="chart-minimal-title">Risk Trend</span>
            <span class="chart-minimal-badge">Over Time</span>
        </div>
        <div class="chart-minimal-container">
    """, unsafe_allow_html=True)
    
    trend_df = (
        df
        .sort_values("timestamp")
        .groupby("timestamp", as_index=False)
        ["risk_probability"]
        .mean()
    )
    
    fig2 = px.line(
        trend_df,
        x="timestamp",
        y="risk_probability",
        markers=True,
        title=""
    )
    
    fig2.update_layout(
        template="plotly_dark",
        height=400,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Inter, sans-serif", size=12, color="#D1D5DB"),
        xaxis_title="Time",
        yaxis_title="Risk Probability (%)",
        xaxis=dict(
            showgrid=True,
            gridcolor="rgba(99, 102, 241, 0.1)",
            showline=True,
            linecolor="rgba(99, 102, 241, 0.2)"
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor="rgba(99, 102, 241, 0.1)",
            showline=True,
            linecolor="rgba(99, 102, 241, 0.2)",
            range=[0, 100]
        ),
        hovermode='x unified'
    )
    
    fig2.update_traces(
        line=dict(color="#6366F1", width=2.5),
        marker=dict(
            size=8,
            color="#818CF8",
            line=dict(color="#6366F1", width=1.5)
        ),
        fill='tozeroy',
        fillcolor='rgba(99, 102, 241, 0.1)'
    )
    
    st.plotly_chart(
        fig2,
        use_container_width=True,
        config={"displayModeBar": False}
    )
    
    st.markdown("</div></div>", unsafe_allow_html=True)

st.markdown('<div class="analytics-divider"></div>', unsafe_allow_html=True)

# ===================================
# RECENT PREDICTIONS
# ===================================

st.markdown("""
<div class="table-minimal-card">
    <div class="table-minimal-header">
        <div class="table-minimal-header-left">
            <span class="table-minimal-icon">📋</span>
            <span class="table-minimal-title">Prediction History</span>
        </div>
        <div class="table-minimal-badge">
            Recent Records
        </div>
    </div>
    <div class="table-minimal-container">
""", unsafe_allow_html=True)

display_df = df[
    [
        "age",
        "attendance",
        "study_hours",
        "previous_grades",
        "risk_probability",
        "risk_level",
        "timestamp"
    ]
].copy()

display_df["risk_probability"] = (
    display_df["risk_probability"]
    .round(2)
)

# Rename columns for better display
display_df.columns = [
    "Age",
    "Attendance",
    "Study Hours",
    "Previous Grades",
    "Risk %",
    "Risk Level",
    "Timestamp"
]

# Style the dataframe using map() instead of applymap()
def color_risk_level(val):
    """Apply color coding to risk levels"""
    if val == "High Risk":
        return 'color: #EF4444; font-weight: 600'
    elif val == "Medium Risk":
        return 'color: #F59E0B; font-weight: 600'
    elif val == "Low Risk":
        return 'color: #10B981; font-weight: 600'
    return ''

styled_df = display_df.style.map(
    color_risk_level,
    subset=["Risk Level"]
)

st.dataframe(
    styled_df,
    use_container_width=True,
    hide_index=True,
    height=400
)

st.markdown("</div></div>", unsafe_allow_html=True)

# Optional: Add export functionality
col1, col2, col3 = st.columns([1, 1, 4])
with col1:
    if st.button("📥 Export CSV", key="export_csv"):
        csv = display_df.to_csv(index=False)
        st.download_button(
            label="Download",
            data=csv,
            file_name="predictions_history.csv",
            mime="text/csv",
            key="download_csv"
        )