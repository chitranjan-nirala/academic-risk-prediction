import streamlit as st

def render_kpi_cards():

    col1, col2, col3, col4 = st.columns(4)

    cards = [
        {
            "title": "Dataset Size",
            "value": "1M",
            "sub": "Student Records",
            "icon": "🗂️"
        },
        {
            "title": "Model Accuracy",
            "value": "86.94%",
            "sub": "Logistic Regression",
            "icon": "🎯"
        },
        {
            "title": "At-Risk Rate",
            "value": "25%",
            "sub": "Of Student Cohort",
            "icon": "⚠️"
        },
        {
            "title": "Algorithm",
            "value": "Logistic",
            "sub": "Regression",
            "icon": "🤖"
        },
    ]

    for col, card in zip([col1, col2, col3, col4], cards):

        with col:

            st.markdown(
                f"""
                <div class="kpi-card">
                    <div class="kpi-top">
                        <div class="kpi-label">{card['title']}</div>
                        <div class="kpi-icon">{card['icon']}</div>
                    </div>
                    <div class="kpi-value">{card['value']}</div>
                    <div class="kpi-sub">{card['sub']}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )