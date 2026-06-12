from src.components.recommendation_engine import (
    RecommendationEngine
)

student_data = {
    "Attendance": 60,
    "Study_Hours": 5,
    "Assignments_Completed": 2,
    "Participation": "Low",
    "Previous_Grades": 45,
    "Internet_Access": "No",
    "Family_Support": "Low"
}

engine = RecommendationEngine()

result = engine.generate_recommendations(
    student_data,
    prediction=1
)

print(result)