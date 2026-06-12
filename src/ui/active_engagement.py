import streamlit as st

def render_active_engagement():
    """
    Renders active engagement input form with consistent minimal styling.
    Original logic preserved - returns dictionary with engagement metrics.
    """

    st.markdown("""
    <div class="engagement-minimal-card">
        <div class="engagement-minimal-header">
            <span class="engagement-minimal-icon">📈</span>
            <span class="engagement-minimal-title">Active Engagement</span>
            <span class="engagement-minimal-badge">Current Term</span>
        </div>
        <div class="engagement-minimal-container">
    """, unsafe_allow_html=True)

    attendance = st.slider(
        "Attendance Rate (%)",
        min_value=0,
        max_value=100,
        value=82,
        key="ae_attendance"
    )

    col1, col2 = st.columns(2)

    with col1:
        study_hours = st.number_input(
            "Weekly Study Hours",
            min_value=0,
            max_value=40,
            value=15,
            key="ae_study"
        )

    with col2:
        participation = st.selectbox(
            "Class Participation",
            ["Low", "Medium", "High"],
            index=1,
            key="ae_participation"
        )

    st.markdown("""
        </div>
    </div>
    """, unsafe_allow_html=True)

    return {
        "Attendance": attendance,
        "Study_Hours": study_hours,
        "Participation": participation,
    }