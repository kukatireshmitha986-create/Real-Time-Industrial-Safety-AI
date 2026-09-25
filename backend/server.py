from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import sqlite3
import os

# ============================================================
# INDUSTRIAL SAFETY AI
# FASTAPI BACKEND
# ============================================================

app = FastAPI(
    title="Industrial Safety AI API",
    description="AI-Powered Real-Time Industrial Safety Monitoring System",
    version="1.0.0"
)

# ============================================================
# CORS
# ============================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# ============================================================
# PROJECT PATHS
# ============================================================

PROJECT_ROOT = r"D:\Real-Time-Industrial-Safety-AI"

DATABASE_PATH = os.path.join(
    PROJECT_ROOT,
    "detections",
    "safety_events.db"
)

SCREENSHOTS_PATH = os.path.join(
    PROJECT_ROOT,
    "screenshots"
)

os.makedirs(SCREENSHOTS_PATH, exist_ok=True)

# ============================================================
# SERVE SCREENSHOTS
# ============================================================

app.mount(
    "/screenshots",
    StaticFiles(directory=SCREENSHOTS_PATH),
    name="screenshots"
)

# ============================================================
# DATABASE
# ============================================================

def get_database():

    connection = sqlite3.connect(
        DATABASE_PATH
    )

    connection.row_factory = sqlite3.Row

    return connection


# ============================================================
# HOME
# ============================================================

@app.get("/")
def home():

    return {
        "status": "success",
        "message": "Industrial Safety AI Backend is running",
        "project": "AI-Powered Real-Time Industrial Safety Monitoring System"
    }


# ============================================================
# HEALTH
# ============================================================

@app.get("/api/health")
def health():

    return {
        "status": "success",
        "backend": "running",
        "database": "SQLite",
        "database_exists": os.path.exists(DATABASE_PATH),
        "screenshots_exists": os.path.exists(SCREENSHOTS_PATH)
    }


# ============================================================
# FORMAT EVENT
# ============================================================

def format_event(row):

    screenshot_path = row["screenshot_path"]

    # Extract only filename
    if screenshot_path:

        filename = os.path.basename(
            screenshot_path.replace("\\", "/")
        )

    else:

        filename = None

    # Check whether screenshot actually exists
    screenshot_exists = False

    if filename:

        full_path = os.path.join(
            SCREENSHOTS_PATH,
            filename
        )

        screenshot_exists = os.path.isfile(
            full_path
        )

    return {
        "id": row["id"],
        "timestamp": row["timestamp"],
        "violation_type": row["violation_type"],
        "confidence": row["confidence"],
        "screenshot_path": screenshot_path,
        "screenshot_exists": screenshot_exists,
        "screenshot_url": (
            f"/screenshots/{filename}"
            if screenshot_exists
            else None
        ),
        "status": row["status"]
    }


# ============================================================
# ALL EVENTS
# ============================================================

@app.get("/api/events")
def get_events():

    connection = get_database()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            id,
            timestamp,
            violation_type,
            confidence,
            screenshot_path,
            status
        FROM safety_events
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    connection.close()

    events = [
        format_event(row)
        for row in rows
    ]

    return {
        "status": "success",
        "count": len(events),
        "events": events
    }


# ============================================================
# RECENT EVENTS
# ============================================================

@app.get("/api/events/recent")
def get_recent_events():

    connection = get_database()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            id,
            timestamp,
            violation_type,
            confidence,
            screenshot_path,
            status
        FROM safety_events
        ORDER BY id DESC
        LIMIT 10
    """)

    rows = cursor.fetchall()

    connection.close()

    events = [
        format_event(row)
        for row in rows
    ]

    return {
        "status": "success",
        "count": len(events),
        "events": events
    }


# ============================================================
# EVENT COUNT
# ============================================================

@app.get("/api/events/count")
def get_event_count():

    connection = get_database()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT COUNT(*) AS total
        FROM safety_events
    """)

    result = cursor.fetchone()

    connection.close()

    return {
        "status": "success",
        "total_violations": result["total"]
    }


# ============================================================
# SINGLE EVENT
# ============================================================

@app.get("/api/events/{event_id}")
def get_event(event_id: int):

    connection = get_database()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            id,
            timestamp,
            violation_type,
            confidence,
            screenshot_path,
            status
        FROM safety_events
        WHERE id = ?
    """, (event_id,))

    row = cursor.fetchone()

    connection.close()

    if row is None:

        return {
            "status": "error",
            "message": "Event not found"
        }

    return {
        "status": "success",
        "event": format_event(row)
    }


# ============================================================
# SERVER
# ============================================================

if __name__ == "__main__":

    import uvicorn

    print("=" * 60)
    print("INDUSTRIAL SAFETY AI BACKEND")
    print("=" * 60)

    print()
    print("Database:")
    print(DATABASE_PATH)

    print()
    print("Screenshots:")
    print(SCREENSHOTS_PATH)

    print()
    print("Screenshots directory exists:")
    print(os.path.exists(SCREENSHOTS_PATH))

    print()
    print("Starting FastAPI server...")
    print("API: http://127.0.0.1:8000")
    print("Docs: http://127.0.0.1:8000/docs")

    print("=" * 60)

    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8000
    )