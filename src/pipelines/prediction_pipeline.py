import pandas as pd
from src.utils.common import load_object


class PredictPipeline:

    def __init__(self):

        self.model = load_object(
            "artifacts/model.pkl"
        )

        self.preprocessor = load_object(
            "artifacts/preprocessor.pkl"
        )

    #prediction method
    def predict(self, features):

        try:

            data_scaled = self.preprocessor.transform(
            features
            )

            prediction = self.model.predict(
            data_scaled
            )

            probability = self.model.predict_proba(
            data_scaled
            )

            return (
            prediction,
            probability
            )

        except Exception as e:
            raise e

    def get_model(self):
        return self.model

    def get_preprocessor(self):
        return self.preprocessor    
    
#create input schema for prediction pipeline
class CustomData:

    def __init__(
        self,
        Age,
        Gender,
        Attendance,
        Study_Hours,
        Assignments_Completed,
        Participation,
        Previous_Grades,
        Internet_Access,
        Family_Support
    ):

        self.Age = Age
        self.Gender = Gender
        self.Attendance = Attendance
        self.Study_Hours = Study_Hours
        self.Assignments_Completed = Assignments_Completed
        self.Participation = Participation
        self.Previous_Grades = Previous_Grades
        self.Internet_Access = Internet_Access
        self.Family_Support = Family_Support

#method to convert input data to dataframe
    def get_data_as_dataframe(self):

        data = {
        "Age": [self.Age],
        "Gender": [self.Gender],
        "Attendance": [self.Attendance],
        "Study_Hours": [self.Study_Hours],
        "Assignments_Completed": [self.Assignments_Completed],
        "Participation": [self.Participation],
        "Previous_Grades": [self.Previous_Grades],
        "Internet_Access": [self.Internet_Access],
        "Family_Support": [self.Family_Support]
       }

        return pd.DataFrame(data)
