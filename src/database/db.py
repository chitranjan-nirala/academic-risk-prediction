import sqlite3
import pandas as pd

class PredictionDatabase:

    def __init__(self):
        self.conn = sqlite3.connect(
            "prediction_history.db",
            check_same_thread=False
        )
        self.create_table()

    # ===================================
    # CREATE TABLE
    # ===================================

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS predictions(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            age INTEGER,
            attendance REAL,
            study_hours REAL,
            previous_grades REAL,
            risk_probability REAL,
            risk_level TEXT,
            intervention_status TEXT DEFAULT 'Pending',
            mentor_assigned TEXT DEFAULT 'Not Assigned'
        )
        """)
        self.conn.commit()

    # ===================================
    # SAVE PREDICTION
    # ===================================

    def save_prediction(
        self,
        student_data,
        risk_probability,
        risk_level
    ):
        cursor = self.conn.cursor()
        cursor.execute("""
        INSERT INTO predictions(
            age,
            attendance,
            study_hours,
            previous_grades,
            risk_probability,
            risk_level
        )
        VALUES(?,?,?,?,?,?)
        """,
        (
            student_data["Age"],
            student_data["Attendance"],
            student_data["Study_Hours"],
            student_data["Previous_Grades"],
            risk_probability,
            risk_level
        ))
        self.conn.commit()

    # ===================================
    # GET ALL PREDICTIONS
    # ===================================

    def get_predictions_dataframe(self):
        query = """
        SELECT *
        FROM predictions
        ORDER BY timestamp DESC
        """
        return pd.read_sql_query(
            query,
            self.conn
        )

    # ===================================
    # UPDATE INTERVENTION
    # ===================================

    def update_intervention(
        self,
        student_id,
        status,
        mentor
    ):
        cursor = self.conn.cursor()
        cursor.execute(
            """
            UPDATE predictions
            SET
                intervention_status=?,
                mentor_assigned=?
            WHERE id=?
            """,
            (
                status,
                mentor,
                student_id
            )
        )
        self.conn.commit()

    # ===================================
    # HIGH RISK STUDENTS
    # ===================================

    def get_high_risk_students(self):
        query = """
        SELECT *
        FROM predictions
        WHERE risk_level='At Risk'
        ORDER BY risk_probability DESC
        """
        return pd.read_sql_query(
            query,
            self.conn
        )

    # ===================================
    # DASHBOARD METRICS
    # ===================================

    def get_total_predictions(self):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT COUNT(*) FROM predictions"
        )
        return cursor.fetchone()[0]

    def get_average_risk(self):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT AVG(risk_probability) FROM predictions"
        )
        result = cursor.fetchone()[0]
        return round(result, 2) if result else 0

    def get_pending_cases(self):
        cursor = self.conn.cursor()
        cursor.execute("""
        SELECT COUNT(*)
        FROM predictions
        WHERE intervention_status='Pending'
        """)
        return cursor.fetchone()[0]

    def get_resolved_cases(self):
        cursor = self.conn.cursor()
        cursor.execute("""
        SELECT COUNT(*)
        FROM predictions
        WHERE intervention_status='Resolved'
        """)
        return cursor.fetchone()[0]

    # ===================================
    # CLOSE CONNECTION
    # ===================================

    def close_connection(self):
        self.conn.close()