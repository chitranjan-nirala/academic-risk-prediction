import streamlit as st
import plotly.graph_objects as go

def render_risk_gauge(risk_probability):
    """
    Original logic preserved — UNCHANGED:
      risk_level thresholds: >=70 HIGH, >=40 MEDIUM, else LOW
      confidence = max(risk_probability, 100 - risk_probability)
    """

    # ── Original logic — UNCHANGED ──
    if risk_probability >= 70:
        risk_level = "HIGH"
        badge_color = "#EF4444"
        bg_opacity = "rgba(239, 68, 68, 0.1)"

    elif risk_probability >= 40:
        risk_level = "MEDIUM"
        badge_color = "#F59E0B"
        bg_opacity = "rgba(245, 158, 11, 0.1)"

    else:
        risk_level = "LOW"
        badge_color = "#10B981"
        bg_opacity = "rgba(16, 185, 129, 0.1)"

    confidence = max(risk_probability, 100 - risk_probability)

    # ── Plotly gauge with FIXED tickcolor ──
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=risk_probability,
        number={
            "suffix": "%",
            "font": {"size": 28, "color": "#F3F4F6", "family": "Inter"},
        },
        title={
            "text": "",
            "font": {"size": 16, "color": badge_color, "family": "Inter"},
        },
        gauge={
            "axis": {
                "range": [0, 100],
                "showticklabels": False,
                "tickwidth": 0,
                # "tickcolor": "rgba(0,0,0,0)",  # FIXED: 'transparent' -> rgba
            },
            "bar": {"color": badge_color, "thickness": 0.24},
            "bgcolor": "rgba(99, 102, 241, 0.05)",
            "borderwidth": 0,
            "steps": [{"range": [0, 100], "color": "rgba(99, 102, 241, 0.03)"}],
            "threshold": {
                "line": {"color": badge_color, "width": 2},
                "thickness": 0.6,
                "value": risk_probability,
            }
        },
    ))

    fig.update_layout(
        height=160,
        margin=dict(t=20, b=4, l=10, r=10),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font={"family": "Inter, sans-serif"},
    )

    # Rest of your rendering code...
    st.markdown(
        f"""
        <div class="gauge-minimal-card">
            <div class="gauge-minimal-header">
                <span class="gauge-minimal-icon">📊</span>
                <span class="gauge-minimal-title">Risk Assessment</span>
                <span class="gauge-minimal-badge" style="background: {bg_opacity}; color: {badge_color};">
                    {risk_level} RISK
                </span>
            </div>
            <div class="gauge-minimal-container">
        """,
        unsafe_allow_html=True,
    )

    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

    st.markdown(
        f"""
            <div class="gauge-minimal-footer">
                <div class="gauge-confidence">
                    <span class="confidence-label">Model Confidence</span>
                    <span class="confidence-value" style="color: {badge_color};">{confidence:.1f}%</span>
                </div>
            </div>
        </div>
        </div>
        """,
        unsafe_allow_html=True,
    )