import streamlit as st
import json
import pandas as pd
import plotly.express as px
from src.ui.sidebar  import render_sidebar
from src.ui.styles import load_css

st.set_page_config(
    page_title="Model Performance",
    page_icon="📈",
    layout="wide"
)

load_css()

# ===================================
# SIDEBAR - 
# ===================================
render_sidebar()  

# Custom header with consistent styling
st.markdown("""
<div class="performance-header-card">
    <div class="performance-header-left">
        <div class="performance-header-icon">📈</div>
        <div>
            <div class="performance-header-title">Model Performance Dashboard</div>
            <div class="performance-header-subtitle">Evaluation metrics & model comparison</div>
        </div>
    </div>
    <div class="performance-header-right">
        <div class="performance-header-badge">Production Ready</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ===================================
# LOAD METRICS
# ===================================
with open("artifacts/metrics.json", "r") as f:
    metrics = json.load(f)

# ===================================
# LOGISTIC REGRESSION KPI
# ===================================
best_model = metrics["Logistic Regression"]

st.markdown("""
<div class="performance-section-header">
    <div class="section-header-icon">🏆</div>
    <div class="section-header-content">
        <div class="section-header-title">Best Performing Model</div>
        <div class="section-header-subtitle">Logistic Regression</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Custom metric cards
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(f"""
    <div class="performance-metric-card">
        <div class="metric-icon">🎯</div>
        <div class="metric-value">{best_model['accuracy']:.2%}</div>
        <div class="metric-label">Accuracy</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="performance-metric-card">
        <div class="metric-icon">📊</div>
        <div class="metric-value">{best_model['precision']:.2%}</div>
        <div class="metric-label">Precision</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="performance-metric-card">
        <div class="metric-icon">🔍</div>
        <div class="metric-value">{best_model['recall']:.2%}</div>
        <div class="metric-label">Recall</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown(f"""
    <div class="performance-metric-card">
        <div class="metric-icon">⚖️</div>
        <div class="metric-value">{best_model['f1_score']:.2%}</div>
        <div class="metric-label">F1 Score</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="performance-divider"></div>', unsafe_allow_html=True)

# ===================================
# MODEL COMPARISON TABLE
# ===================================

st.markdown("""
<div class="performance-table-card">
    <div class="performance-table-header">
        <div class="performance-table-header-left">
            <span class="performance-table-icon">📋</span>
            <span class="performance-table-title">Model Comparison</span>
        </div>
        <div class="performance-table-badge">All Models</div>
    </div>
    <div class="performance-table-container">
""", unsafe_allow_html=True)

comparison_df = (
    pd.DataFrame(metrics)
    .T
    .reset_index()
)

comparison_df.columns = [
    "Model",
    "Accuracy",
    "Precision",
    "Recall",
    "F1 Score"
]

# Style the dataframe to highlight the best model
def highlight_best_model(row):
    if row["Model"] == "Logistic Regression":
        return ['background-color: rgba(99, 102, 241, 0.15); font-weight: 600'] * len(row)
    return [''] * len(row)

styled_comparison = comparison_df.style.apply(highlight_best_model, axis=1)

# Format percentage columns
styled_comparison = styled_comparison.format({
    "Accuracy": "{:.2%}",
    "Precision": "{:.2%}",
    "Recall": "{:.2%}",
    "F1 Score": "{:.2%}"
})

st.dataframe(
    styled_comparison,
    use_container_width=True,
    hide_index=True,
    height=300
)

st.markdown("</div></div>", unsafe_allow_html=True)

st.markdown('<div class="performance-divider"></div>', unsafe_allow_html=True)

# ===================================
# MODEL COMPARISON CHART
# ===================================

st.markdown("""
<div class="performance-chart-card">
    <div class="performance-chart-header">
        <div class="performance-chart-header-left">
            <span class="performance-chart-icon">📊</span>
            <span class="performance-chart-title">Performance Comparison</span>
        </div>
        <div class="performance-chart-badge">Visual Analysis</div>
    </div>
    <div class="performance-chart-container">
""", unsafe_allow_html=True)

chart_df = comparison_df.melt(
    id_vars="Model",
    var_name="Metric",
    value_name="Score"
)

# Custom color palette
color_palette = {
    "Logistic Regression": "#6366F1",
    "Random Forest": "#10B981",
    "XGBoost": "#F59E0B",
    "SVM": "#EF4444"
}

fig = px.bar(
    chart_df,
    x="Metric",
    y="Score",
    color="Model",
    barmode="group",
    title="",
    color_discrete_map=color_palette
)

fig.update_layout(
    template="plotly_dark",
    height=500,
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="Inter, sans-serif", size=12, color="#D1D5DB"),
    xaxis_title="Metric",
    yaxis_title="Score",
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
        tickformat='.0%',
        range=[0, 1]
    ),
    legend=dict(
        bgcolor="rgba(17, 19, 24, 0.8)",
        bordercolor="rgba(99, 102, 241, 0.2)",
        borderwidth=1,
        font=dict(size=11)
    ),
    hovermode='x unified'
)

fig.update_traces(
    marker=dict(line=dict(color='rgba(17, 19, 24, 0.8)', width=1.5))
)

st.plotly_chart(
    fig,
    use_container_width=True,
    config={"displayModeBar": False}
)

st.markdown("</div></div>", unsafe_allow_html=True)

st.markdown('<div class="performance-divider"></div>', unsafe_allow_html=True)

# ===================================
# CONFUSION MATRIX & ROC CURVE
# ===================================

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="performance-image-card">
        <div class="performance-image-header">
            <div class="performance-image-header-left">
                <span class="performance-image-icon">📊</span>
                <span class="performance-image-title">Confusion Matrix</span>
            </div>
            <div class="performance-image-badge">Predictions vs Actual</div>
        </div>
        <div class="performance-image-container">
    """, unsafe_allow_html=True)
    
    st.image(
        "artifacts/confusion_matrix.png",
        use_container_width=True
    )
    
    st.markdown("</div></div>", unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="performance-image-card">
        <div class="performance-image-header">
            <div class="performance-image-header-left">
                <span class="performance-image-icon">📈</span>
                <span class="performance-image-title">ROC Curve</span>
            </div>
            <div class="performance-image-badge">Model Discrimination</div>
        </div>
        <div class="performance-image-container">
    """, unsafe_allow_html=True)
    
    st.image(
        "artifacts/roc_curve.png",
        use_container_width=True
    )
    
    st.markdown("</div></div>", unsafe_allow_html=True)

st.markdown('<div class="performance-divider"></div>', unsafe_allow_html=True)

# ===================================
# INSIGHTS
# ===================================

st.markdown("""
<div class="performance-insights-card">
    <div class="performance-insights-header">
        <div class="performance-insights-header-left">
            <span class="performance-insights-icon">📌</span>
            <span class="performance-insights-title">Model Insights</span>
        </div>
        <div class="performance-insights-badge">Key Findings</div>
    </div>
    <div class="performance-insights-container">
        <div class="insight-item">
            <div class="insight-icon">🏆</div>
            <div class="insight-text">Logistic Regression achieved the best overall balance between Accuracy, Precision, Recall, and F1 Score.</div>
        </div>
        <div class="insight-item">
            <div class="insight-icon">📈</div>
            <div class="insight-text">The ROC-AUC score exceeds 0.92, indicating excellent separation between at-risk and non-risk students.</div>
        </div>
        <div class="insight-item">
            <div class="insight-icon">⚡</div>
            <div class="insight-text">Model demonstrates strong predictive power with minimal overfitting across validation sets.</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)