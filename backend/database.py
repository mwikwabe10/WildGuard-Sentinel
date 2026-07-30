import sqlite3

DB_NAME = "wildguard.db"


def init_db():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()


    # Existing detections

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS detections (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        filename TEXT,

        category TEXT,

        confidence REAL,

        latitude REAL,

        longitude REAL,

        timestamp TEXT

    )
    """)


    # Alerts

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS alerts (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        alert_level TEXT,

        message TEXT,

        latitude REAL,

        longitude REAL,

        timestamp TEXT

    )
    """)


    # Cameras

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cameras (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        camera_id TEXT,

        name TEXT,

        latitude REAL,

        longitude REAL,

        location TEXT,

        status TEXT

    )
    """)


    # Users

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT,

        role TEXT

    )
    """)


    # Protected Areas

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS protected_areas (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT,

        latitude REAL,

        longitude REAL,

        radius REAL

    )
    """)


    # INCIDENT TABLE

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS incidents (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        incident_type TEXT,

        category TEXT,

        description TEXT,

        latitude REAL,

        longitude REAL,

        severity TEXT,

        reported_by TEXT,

        status TEXT,

        timestamp TEXT

    )
    """)


    conn.commit()

    conn.close()