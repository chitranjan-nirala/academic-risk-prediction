import streamlit as st
import pandas as pd
import plotly.express as px
from src.ui.sidebar  import render_sidebar
from src.database.db import PredictionDatabase
from src.ui.styles import load_css

# Page setup and title
st.set_page_config(
    page_title="Student Segmentation",
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
<div class="segmentation-header-card">
    <div class="segmentation-header-left">
        <div class="segmentation-header-icon">🎯</div>
        <div>
            <div class="segmentation-header-title">Student Segmentation Dashboard</div>
            <div class="segmentation-header-subtitle">Analyze risk patterns across student segments</div>
        </div>
    </div>
    <div class="segmentation-header-right">
        <div class="segmentation-header-badge">Cluster Analysis</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Load data
db = PredictionDatabase()
df = db.get_predictions_dataframe()

if df.empty:
    st.markdown("""
    <div class="segmentation-empty-state">
        <div class="empty-state-icon">📭</div>
        <div class="empty-state-title">No Data Available</div>
        <div class="empty-state-text">Generate predictions to view student segmentation analysis.</div>
    </div>
    """, unsafe_allow_html=True)
    st.stop()

# ===================================
# ATTENDANCE VS RISK
# ===================================

st.markdown("""
<div class="segmentation-chart-card">
    <div class="segmentation-chart-header">
        <div class="segmentation-chart-header-left">
            <span class="segmentation-chart-icon">📊</span>
            <span class="segmentation-chart-title">Attendance vs Risk Profile</span>
        </div>
        <div class="segmentation-chart-badge">Correlation Analysis</div>
    </div>
    <div class="segmentation-chart-container">
""", unsafe_allow_html=True)

fig1 = px.scatter(
    df,
    x="attendance",
    y="risk_probability",
    color="risk_level",
    size="study_hours",
    hover_data=["previous_grades", "age"],
    title=""
)

# Custom color mapping
color_map = {
    "High Risk": "#EF4444",
    "Medium Risk": "#F59E0B",
    "Low Risk": "#10B981"
}

fig1.update_layout(
    template="plotly_dark",
    height=500,
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="Inter, sans-serif", size=12, color="#D1D5DB"),
    xaxis_title="Attendance Rate (%)",
    yaxis_title="Risk Probability (%)",
    xaxis=dict(
        showgrid=True,
        gridcolor="rgba(99, 102, 241, 0.1)",
        showline=True,
        linecolor="rgba(99, 102, 241, 0.2)",
        range=[0, 100]
    ),
    yaxis=dict(
        showgrid=True,
        gridcolor="rgba(99, 102, 241, 0.1)",
        showline=True,
        linecolor="rgba(99, 102, 241, 0.2)",
        range=[0, 100]
    ),
    legend=dict(
        bgcolor="rgba(17, 19, 24, 0.8)",
        bordercolor="rgba(99, 102, 241, 0.2)",
        borderwidth=1,
        font=dict(size=11)
    ),
    hovermode='closest'
)

fig1.update_traces(
    marker=dict(
        line=dict(color='rgba(17, 19, 24, 0.8)', width=1.5),
        opacity=0.7
    )
)

st.plotly_chart(fig1, use_container_width=True, config={"displayModeBar": False})

st.markdown("</div></div>", unsafe_allow_html=True)

st.markdown('<div class="segmentation-divider"></div>', unsafe_allow_html=True)

# ===================================
# GRADES VS RISK
# ===================================

st.markdown("""
<div class="segmentation-chart-card">
    <div class="segmentation-chart-header">
        <div class="segmentation-chart-header-left">
            <span class="segmentation-chart-icon">📚</span>
            <span class="segmentation-chart-title">Previous Grades vs Risk Profile</span>
        </div>
        <div class="segmentation-chart-badge">Performance Analysis</div>
    </div>
    <div class="segmentation-chart-container">
""", unsafe_allow_html=True)

fig2 = px.scatter(
    df,
    x="previous_grades",
    y="risk_probability",
    color="risk_level",
    color_discrete_map=color_map,
    title=""
)

fig2.update_layout(
    template="plotly_dark",
    height=500,
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="Inter, sans-serif", size=12, color="#D1D5DB"),
    xaxis_title="Previous Grades (%)",
    yaxis_title="Risk Probability (%)",
    xaxis=dict(
        showgrid=True,
        gridcolor="rgba(99, 102, 241, 0.1)",
        showline=True,
        linecolor="rgba(99, 102, 241, 0.2)",
        range=[0, 100]
    ),
    yaxis=dict(
        showgrid=True,
        gridcolor="rgba(99, 102, 241, 0.1)",
        showline=True,
        linecolor="rgba(99, 102, 241, 0.2)",
        range=[0, 100]
    ),
    legend=dict(
        bgcolor="rgba(17, 19, 24, 0.8)",
        bordercolor="rgba(99, 102, 241, 0.2)",
        borderwidth=1,
        font=dict(size=11)
    )
)

fig2.update_traces(
    marker=dict(
        size=10,
        line=dict(color='rgba(17, 19, 24, 0.8)', width=1.5),
        opacity=0.7
    )
)

st.plotly_chart(fig2, use_container_width=True, config={"displayModeBar": False})

st.markdown("</div></div>", unsafe_allow_html=True)

st.markdown('<div class="segmentation-divider"></div>', unsafe_allow_html=True)

# ===================================
# STUDY HOURS VS RISK
# ===================================

st.markdown("""
<div class="segmentation-chart-card">
    <div class="segmentation-chart-header">
        <div class="segmentation-chart-header-left">
            <span class="segmentation-chart-icon">⏰</span>
            <span class="segmentation-chart-title">Study Hours Distribution by Risk Level</span>
        </div>
        <div class="segmentation-chart-badge">Box Plot Analysis</div>
    </div>
    <div class="segmentation-chart-container">
""", unsafe_allow_html=True)

fig3 = px.box(
    df,
    x="risk_level",
    y="study_hours",
    color="risk_level",
    color_discrete_map=color_map,
    title=""
)

fig3.update_layout(
    template="plotly_dark",
    height=500,
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="Inter, sans-serif", size=12, color="#D1D5DB"),
    xaxis_title="Risk Level",
    yaxis_title="Weekly Study Hours",
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
        range=[0, 40]
    ),
    legend=dict(
        bgcolor="rgba(17, 19, 24, 0.8)",
        bordercolor="rgba(99, 102, 241, 0.2)",
        borderwidth=1,
        font=dict(size=11)
    ),
    showlegend=False
)

fig3.update_traces(
    marker=dict(
        outliercolor="#EF4444",
        line=dict(color='rgba(17, 19, 24, 0.8)', width=1.5)
    )
)

st.plotly_chart(fig3, use_container_width=True, config={"displayModeBar": False})

st.markdown("</div></div>", unsafe_allow_html=True)

st.markdown('<div class="segmentation-divider"></div>', unsafe_allow_html=True)

# ===================================
# AGE GROUP ANALYSIS
# ===================================

st.markdown("""
<div class="segmentation-chart-card">
    <div class="segmentation-chart-header">
        <div class="segmentation-chart-header-left">
            <span class="segmentation-chart-icon">👥</span>
            <span class="segmentation-chart-title">Average Risk by Age Group</span>
        </div>
        <div class="segmentation-chart-badge">Demographic Analysis</div>
    </div>
    <div class="segmentation-chart-container">
""", unsafe_allow_html=True)

# Create age group
df["age_group"] = pd.cut(
    df["age"],
    bins=[15, 18, 21, 24, 30],
    labels=["15-18", "19-21", "22-24", "25-30"]
)

# Chart data
risk_age = (
    df.groupby("age_group", observed=True)
    ["risk_probability"]
    .mean()
    .reset_index()
)

fig4 = px.bar(
    risk_age,
    x="age_group",
    y="risk_probability",
    title="",
    color="risk_probability",
    color_continuous_scale=["#10B981", "#F59E0B", "#EF4444"],
    text="risk_probability"
)

fig4.update_layout(
    template="plotly_dark",
    height=500,
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="Inter, sans-serif", size=12, color="#D1D5DB"),
    xaxis_title="Age Group",
    yaxis_title="Average Risk Probability (%)",
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
        range=[0, 100],
        tickformat='.0f'
    ),
    coloraxis_showscale=False
)

fig4.update_traces(
    texttemplate='%{text:.1f}%',
    textposition='outside',
    marker=dict(line=dict(color='rgba(17, 19, 24, 0.8)', width=1.5))
)

st.plotly_chart(fig4, use_container_width=True, config={"displayModeBar": False})

st.markdown("</div></div>", unsafe_allow_html=True)

st.markdown('<div class="segmentation-divider"></div>', unsafe_allow_html=True)

# ===================================
# TOP RISK STUDENTS
# ===================================

st.markdown("""
<div class="segmentation-table-card">
    <div class="segmentation-table-header">
        <div class="segmentation-table-header-left">
            <span class="segmentation-table-icon">🚨</span>
            <span class="segmentation-table-title">Students Requiring Immediate Intervention</span>
        </div>
        <div class="segmentation-table-badge">Top 10 High Risk</div>
    </div>
    <div class="segmentation-table-container">
""", unsafe_allow_html=True)

high_risk = df.sort_values(
    "risk_probability",
    ascending=False
).head(10)

# Style the dataframe
def color_risk_high(val):
    """Apply color coding to risk probability"""
    if isinstance(val, (int, float)):
        if val >= 70:
            return 'color: #EF4444; font-weight: 700'
        elif val >= 40:
            return 'color: #F59E0B; font-weight: 600'
    return ''

styled_high_risk = high_risk.style.map(
    color_risk_high,
    subset=["risk_probability"]
).format({
    "risk_probability": "{:.1f}%",
    "attendance": "{:.0f}",
    "study_hours": "{:.1f}",
    "previous_grades": "{:.0f}"
})

st.dataframe(
    styled_high_risk,
    use_container_width=True,
    hide_index=True,
    height=400
)

st.markdown("</div></div>", unsafe_allow_html=True)