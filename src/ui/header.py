import streamlit as st
from datetime import date


def render_header():

    d = date.today()
    today = f"{d.strftime('%B')} {d.day}, {d.strftime('%Y')}"

    st.markdown(
        f"""
        <div class="header-card">
            <div class="header-left">
                <div class="header-title">🎓 Academic Risk &amp; Engagement Prediction System</div>
                <div class="header-subtitle">
                    Predict student performance risk and identify engagement interventions.
                </div>
            </div>
            <div class="header-right">
                <div class="header-date">{today}</div>
                <div class="header-year">Academic Year 2025–26</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
