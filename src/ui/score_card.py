import streamlit as st


def render_score_card(risk_probability):
    """
    Original logic preserved — UNCHANGED:
      success_score = int(100 - risk_probability)
      badge thresholds: >=80 Excellent, >=60 Average, else Needs Attention
    Only visual presentation is restyled.
    """

    # ── Original logic — UNCHANGED ──
    success_score = int(100 - risk_probability)

    if success_score >= 80:
        badge_color = "#10B981"
        performance = "Excellent"

    elif success_score >= 60:
        badge_color = "#F59E0B"
        performance = "Average"

    else:
        badge_color = "#EF4444"
        performance = "Needs Attention"

    st.markdown(
        f"""
        <div class="score-card">
            <div class="score-eyebrow">Predicted Exam Score</div>
            <div style="margin: 8px 0 10px;">
                <span class="score-number">{success_score}</span>
                <span class="score-denom"> /100</span>
            </div>
            <div style="
                display: inline-flex;
                align-items: center;
                gap: 6px;
                padding: 7px 16px;
                border-radius: 999px;
                background: {badge_color}20;
                color: {badge_color};
                font-size: 13px;
                font-weight: 700;
                border: 1.5px solid {badge_color}40;
            ">
                {performance}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
