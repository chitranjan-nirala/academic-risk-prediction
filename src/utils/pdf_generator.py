from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


class PDFGenerator:

    @staticmethod
    def generate_report(
        filename,
        student_data,
        risk_probability,
        risk_level,
        observations,
        recommendations
    ):
        
        doc = SimpleDocTemplate(filename)

        styles = getSampleStyleSheet()

        content = []

        content.append(
            Paragraph(
                "Academic Risk Assessment Report",
                styles["Title"]
            )
        )

        content.append(Spacer(1, 12))

        # Student Profile
        content.append(
            Paragraph(
                "Student Profile",
                styles["Heading2"]
            )
        )

        for key, value in student_data.items():

            content.append(
                Paragraph(
                    f"<b>{key}</b>: {value}",
                    styles["BodyText"]
                )
            )

        content.append(Spacer(1, 12))

        # Prediction Result
        content.append(
            Paragraph(
                "Prediction Result",
                styles["Heading2"]
            )
        )

        content.append(
            Paragraph(
                f"Risk Probability: {risk_probability:.2f}%",
                styles["BodyText"]
            )
        )

        content.append(
            Paragraph(
                f"Risk Level: {risk_level}",
                styles["BodyText"]
            )
        )

        content.append(Spacer(1, 12))
        # Observations
        content.append(
            Paragraph(
            "Key Observations",
            styles["Heading2"]
    )
)

        for obs in observations:

            content.append(
            Paragraph(
            f"• {obs}",
            styles["BodyText"]
        )
    )

        content.append(Spacer(1, 12))
        
        # Recommendations
        content.append(
            Paragraph(
                "Recommendations",
                styles["Heading2"]
            )
        )

        if recommendations:

            for rec in recommendations:

                content.append(
                Paragraph(
                f"• {rec}",
                styles["BodyText"]
            )
        )
        else:

             content.append(
             Paragraph(
            "No intervention required.",
            styles["BodyText"]
           )
        )

        doc.build(content)

        return filename