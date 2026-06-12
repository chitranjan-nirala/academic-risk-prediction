import streamlit as st
# ===================================
# IMPORTS
# ===================================
from src.ui.styles               import load_css
from src.ui.header               import render_header
from src.ui.sidebar              import render_sidebar
from src.ui.kpi_cards            import render_kpi_cards
from src.ui.student_profile      import render_student_profile
from src.ui.active_engagement    import render_active_engagement
from src.ui.academic_history     import render_academic_history
from src.ui.score_card           import render_score_card
from src.ui.risk_gauge           import render_risk_gauge
from src.ui.insights_panel       import render_insights
from src.ui.recommendation_panel import render_recommendations
from src.utils.pdf_generator     import PDFGenerator

from src.pipelines.prediction_pipeline    import PredictPipeline, CustomData
from src.components.recommendation_engine import RecommendationEngine
from src.database.db                      import PredictionDatabase


# ===================================
# PAGE CONFIG  (must be first)
# ===================================
st.set_page_config(
    page_title="Academic Risk Prediction",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ===================================
# SESSION STATE
# ===================================
if "profile_generated" not in st.session_state:
    st.session_state.profile_generated = False

# ===================================
# GLOBAL STYLES + DATABASE
# ===================================
load_css()
db = PredictionDatabase()

# ===================================
# SIDEBAR - MUST BE FIRST AFTER LOAD_CSS
# ===================================
render_sidebar()  

# ===================================
# HEADER + KPI STRIP  
# ===================================
render_header()
render_kpi_cards()
st.markdown("<br>", unsafe_allow_html=True)

# ===================================
# MAIN LAYOUT
# ===================================
left_col, right_col = st.columns([1, 1.25])

# -----------------------------------
# LEFT PANEL — input forms
# -----------------------------------
with left_col:

    profile_data    = render_student_profile()
    st.markdown("<br>", unsafe_allow_html=True)

    engagement_data = render_active_engagement()
    st.markdown("<br>", unsafe_allow_html=True)

    academic_data   = render_academic_history()
    st.markdown("<br>", unsafe_allow_html=True)

    predict_btn = st.button(
        "⚡ GENERATE RISK PROFILE",
        use_container_width=True,
    )

    if predict_btn:
        st.session_state.profile_generated = True

# -----------------------------------
# RIGHT PANEL — results dashboard
# -----------------------------------
with right_col:

    if not st.session_state.profile_generated:

        st.markdown("""
        <div class="dashboard-placeholder">
            <div class="placeholder-icon">📊</div>
            <h2>Academic Risk Dashboard</h2>
            <p>
                Complete the student profile and click
                <strong>Generate Risk Profile</strong>
                to view predictive analytics.
            </p>
            <br>
            <p style="font-size:13px; color:#94A3B8;">
                Predicted Exam Score &nbsp;·&nbsp; Risk Probability
                &nbsp;·&nbsp; Explainable Insights &nbsp;·&nbsp; Recommendations
            </p>
        </div>
        """, unsafe_allow_html=True)

    else:

        # ===================================
        # COMBINE FORM DATA  
        # ===================================
        student_data = {
            **profile_data,
            **engagement_data,
            **academic_data,
        }

        # ===================================
        # MODEL INPUT  
        # ===================================
        student = CustomData(
            Age                  = student_data["Age"],
            Gender               = student_data["Gender"],
            Attendance           = student_data["Attendance"],
            Study_Hours          = student_data["Study_Hours"],
            Assignments_Completed= student_data["Assignments_Completed"],
            Participation        = student_data["Participation"],
            Previous_Grades      = student_data["Previous_Grades"],
            Internet_Access      = student_data["Internet_Access"],
            Family_Support       = student_data["Family_Support"],
        )

        data = student.get_data_as_dataframe()

        # ===================================
        # PREDICTION  
        # ===================================
        pipeline = PredictPipeline()
        prediction, probability = pipeline.predict(data)
        risk_probability = probability[0][1] * 100

        # ===================================
        # RECOMMENDATION ENGINE  
        # ===================================
        engine = RecommendationEngine()
        result = engine.generate_recommendations(
            student_data={
                "Attendance"           : student_data["Attendance"],
                "Study_Hours"          : student_data["Study_Hours"],
                "Assignments_Completed": student_data["Assignments_Completed"],
                "Participation"        : student_data["Participation"],
                "Previous_Grades"      : student_data["Previous_Grades"],
                "Internet_Access"      : student_data["Internet_Access"],
                "Family_Support"       : student_data["Family_Support"],
            },
            prediction=int(prediction[0]),
        )

        db.save_prediction(
            student_data,
            risk_probability,
            result["risk_level"]
        )

        # ===================================
        # TOP DASHBOARD CARDS  
        # ===================================
        top_left, top_right = st.columns(2)

        with top_left:
            render_score_card(risk_probability)

        with top_right:
            render_risk_gauge(risk_probability)

        st.markdown("<br>", unsafe_allow_html=True)

        # ===================================
        # INSIGHTS + RECOMMENDATIONS  
        # ===================================
        bottom_left, bottom_right = st.columns(2)

        with bottom_left:
            render_insights(result)

        with bottom_right:
            render_recommendations(result)

            pdf_path = PDFGenerator.generate_report(
                filename="student_risk_report.pdf",
                student_data=student_data,
                risk_probability=risk_probability,
                risk_level=result["risk_level"],
                observations=result["observations"],
                recommendations=result["recommendations"]
            )

            with open(pdf_path, "rb") as pdf_file:
                st.download_button(
                    label="📄 Download Risk Report",
                    data=pdf_file,
                    file_name="student_risk_report.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )