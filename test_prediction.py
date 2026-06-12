from src.pipelines.prediction_pipeline import (
    PredictPipeline,
    CustomData
)
from src.components.recommendation_engine import (
    RecommendationEngine
)


# create a sample input for prediction
student = CustomData(
    Age=20,
    Gender="Male",
    Attendance=60,
    Study_Hours=5,
    Assignments_Completed=2,   # realistic
    Participation="Low",
    Previous_Grades=45,
    Internet_Access="No",
    Family_Support="Low"
)

# convert the input data to a dataframe
data = student.get_data_as_dataframe()

print(data)

#create prediction pipeline object
pipeline = PredictPipeline()

prediction, probability = (
    pipeline.predict(data)
)
#create recommendation engine object
engine = RecommendationEngine()

result = engine.generate_recommendations(
    student_data={
        "Attendance": student.Attendance,
        "Study_Hours": student.Study_Hours,
        "Assignments_Completed": student.Assignments_Completed,
        "Participation": student.Participation,
        "Previous_Grades": student.Previous_Grades,
        "Internet_Access": student.Internet_Access,
        "Family_Support": student.Family_Support
    },
    prediction=int(prediction[0])
)


# Print Prediction Results
print("\n" + "="*50)
print("ACADEMIC RISK PREDICTION RESULT")
print("="*50)

print(f"\nPrediction: {prediction[0]}")

print(
    f"Not At Risk Probability: {probability[0][0]:.4f}"
)

print(
    f"At Risk Probability: {probability[0][1]:.4f}"
)

print(f"\nRisk Level: {result['risk_level']}")

# Print Observations
print("\nObservations:")
for obs in result["observations"]:
    print(f"• {obs}")

# Print Recommendations
print("\nRecommendations:")
for rec in result["recommendations"]:
    print(f"• {rec}")