import sqlite3
import os
from datetime import datetime

# ============================================================
# INDUSTRIAL SAFETY AI
# SQLITE DATABASE
# ============================================================

DATABASE_PATH = "detections/safety_events.db"


# ============================================================
# CREATE DATABASE AND TABLE
# ============================================================

def create_database():

    # Create detections folder
    os.makedirs("detections", exist_ok=True)

    # Connect to SQLite
    connection = sqlite3.connect(DATABASE_PATH)

    cursor = connection.cursor()

    # Create safety events table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS safety_events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            violation_type TEXT NOT NULL,
            confidence REAL,
            screenshot_path TEXT,
            status TEXT DEFAULT 'Open'
        )
    """)

    connection.commit()
    connection.close()

    print("SQLite database initialized successfully.")
    print(f"Database: {DATABASE_PATH}")


# ============================================================
# LOG SAFETY VIOLATION
# ============================================================

def log_violation(
    violation_type,
    confidence,
    screenshot_path
):

    connection = sqlite3.connect(DATABASE_PATH)

    cursor = connection.cursor()

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    cursor.execute("""
        INSERT INTO safety_events
        (
            timestamp,
            violation_type,
            confidence,
            screenshot_path,
            status
        )
        VALUES (?, ?, ?, ?, ?)
    """, (
        timestamp,
        violation_type,
        confidence,
        screenshot_path,
        "Open"
    ))

    connection.commit()

    event_id = cursor.lastrowid

    connection.close()

    print(
        f"[DATABASE] Violation event saved. ID: {event_id}"
    )

    return event_id


# ============================================================
# RUN DATABASE SETUP
# ============================================================

if __name__ == "__main__":

    create_database()

    print()
    print("Database setup completed.")