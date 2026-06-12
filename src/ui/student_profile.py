import streamlit as st

def render_student_profile():
    """
    Renders student profile input form with consistent minimal styling.
    Original logic preserved - returns dictionary with student attributes.
    """

    st.markdown("""
    <div class="profile-minimal-card">
        <div class="profile-minimal-header">
            <span class="profile-minimal-icon">👤</span>
            <span class="profile-minimal-title">Student Profile</span>
            <span class="profile-minimal-badge">Required</span>
        </div>
        <div class="profile-minimal-container">
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input(
            "Age",
            min_value=15,
            max_value=30,
            value=20,
            key="sp_age"
        )

    with col2:
        gender = st.selectbox(
            "Gender",
            ["Male", "Female", "Non-Binary"],
            key="sp_gender"
        )

    internet_access = st.toggle(
        "🛜  Consistent Internet Access",
        value=True,
        key="sp_internet"
    )

    family_support = st.selectbox(
        "Family Support Level",
        ["Low", "Medium", "High"],
        index=1,
        key="sp_family"
    )

    st.markdown("""
        </div>
    </div>
    """, unsafe_allow_html=True)
 
    return {
        "Age": age,
        "Gender": gender,
        "Family_Support": family_support,
        "Internet_Access": "Yes" if internet_access else "No",
    }