class RecommendationEngine:

    def generate_recommendations(
        self,
        student_data,
        prediction
    ):

        observations = []
        recommendations = []

        # Attendance
        if student_data["Attendance"] < 75:
            observations.append(
                "Low attendance detected"
            )

            recommendations.append(
                "Increase class attendance to at least 75%"
            )

        # Study Hours
        if student_data["Study_Hours"] < 10:
            observations.append(
                "Insufficient study hours"
            )

            recommendations.append(
                "Increase study hours to 10-12 hours per week"
            )

        # Assignment Completion
        if student_data["Assignments_Completed"] < 5:
            observations.append(
                "Low assignment completion"
            )

            recommendations.append(
                "Complete pending assignments"
            )

        # Previous Grades
        if student_data["Previous_Grades"] < 60:
            observations.append(
                "Weak academic history"
            )

            recommendations.append(
                "Seek mentoring support and revision sessions"
            )

        # Participation
        if student_data["Participation"] == "Low":
            observations.append(
                "Low classroom participation"
            )

            recommendations.append(
                "Participate more actively in classroom discussions"
            )

        # Internet Access
        if student_data["Internet_Access"] == "No":
            observations.append(
                "Limited internet access"
            )

            recommendations.append(
                "Use campus digital resources whenever possible"
            )

        # Family Support
        if student_data["Family_Support"] == "Low":
            observations.append(
                "Low family support"
            )

            recommendations.append(
                "Connect with academic advisors and peer study groups"
            )

        risk_level = (
            "At Risk"
            if prediction == 1
            else "Not At Risk"
        )

        return {
            "risk_level": risk_level,
            "observations": observations,
            "recommendations": recommendations
        }