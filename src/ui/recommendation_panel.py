import streamlit as st

def render_recommendations(result):
    """
    Iterates result["recommendations"] from the RecommendationEngine.
    Minimal and clean visual presentation.
    """

    recs_html = ""

    for rec in result["recommendations"]:
        recs_html += f"""
        <div class="rec-minimal-item">
            <span class="rec-minimal-check">→</span>
            <span class="rec-minimal-text">{rec}</span>
        </div>"""

    st.markdown(
        f"""
        <div class="rec-minimal-card">
            <div class="rec-minimal-header">
                <span class="rec-minimal-icon">💡</span>
                <span class="rec-minimal-title">Recommendations</span>
            </div>
            <div class="rec-minimal-list">
                {recs_html}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )