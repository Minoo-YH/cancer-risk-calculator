
import os

import psycopg


def get_connection():
    return psycopg.connect(
        host=os.getenv("DB_HOST", "127.0.0.1"),
        port=os.getenv("DB_PORT", "5433"),
        dbname=os.getenv("DB_NAME", "cancer_demo"),
        user=os.getenv("DB_USER", "cancer_app"),
        password=os.environ["DB_PASSWORD"],
        connect_timeout=5,
    )


def save_demo_calculation(age, smoking, family_history, score):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO demo_calculations
                    (age, smoking_status, family_history, demo_score)
                VALUES (%s, %s, %s, %s)
                RETURNING id
                """,
                (age, smoking, family_history, score),
            )
            return cursor.fetchone()[0]
