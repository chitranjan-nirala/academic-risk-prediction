import streamlit as st

def render_academic_history():
    """
    Renders academic history input form with consistent minimal styling.
    Original logic preserved - returns dictionary with academic metrics.
    """

    st.markdown("""
    <div class="academic-minimal-card">
        <div class="academic-minimal-header">
            <span class="academic-minimal-icon">🎓</span>
            <span class="academic-minimal-title">Academic History</span>
            <span class="academic-minimal-badge">Previous Term</span>
        </div>
        <div class="academic-minimal-container">
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        previous_grades = st.number_input(
            "Previous Grades (0–100)",
            min_value=0,
            max_value=100,
            value=75,
            key="ah_grades"
        )

    with col2:
        assignments_completed = st.number_input(
            "Assignments Completed",
            min_value=0,
            max_value=10,
            value=7,
            key="ah_tasks"
        )

    st.markdown("""
        </div>
    </div>
    """, unsafe_allow_html=True)

    return {
        "Previous_Grades": previous_grades,
        "Assignments_Completed": assignments_completed,
    }