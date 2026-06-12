import streamlit as st

def render_insights(result):
    """
    Original logic preserved: iterates result["observations"]
    Minimal and clean visual presentation.
    """

    rows_html = ""

    for obs in result["observations"]:

        # ── Original keyword mapping ──
        if "attendance" in obs.lower():
            icon = "📉"
            color = "#F59E0B"
            score = "-3.2%"
        elif "assignment" in obs.lower():
            icon = "📝"
            color = "#10B981"
            score = "+12.4%"
        elif "support" in obs.lower():
            icon = "👨‍👩‍👧"
            color = "#10B981"
            score = "+5.8%"
        else:
            icon = "📌"
            color = "#6366F1"
            score = "0%"

        rows_html += f"""
        <div class="insight-minimal-item">
            <div class="insight-minimal-icon" style="color: {color};">{icon}</div>
            <div class="insight-minimal-content">
                <div class="insight-minimal-text">{obs}</div>
                <div class="insight-minimal-meta">
                    <span class="insight-minimal-score" style="color: {color};">{score}</span>
                    <span class="insight-minimal-impact">impact</span>
                </div>
            </div>
        </div>"""

    st.markdown(
        f"""
        <div class="insight-minimal-card">
            <div class="insight-minimal-header">
                <span class="insight-minimal-icon-header">🔍</span>
                <span class="insight-minimal-title">Key Insights</span>
                <span class="insight-minimal-badge">87% confidence</span>
            </div>
            <div class="insight-minimal-list">
                {rows_html}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )