import sqlite3

DB_NAME = "wildguard.db"


def save_detection(
    filename,
    category,
    confidence,
    latitude,
    longitude,
    timestamp
):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO detections
        (
            filename,
            category,
            confidence,
            latitude,
            longitude,
            timestamp
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            filename,
            category,
            confidence,
            latitude,
            longitude,
            timestamp
        )
    )

    conn.commit()
    conn.close()



def save_alert(
    level,
    message,
    latitude,
    longitude,
    timestamp
):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO alerts
        (
            alert_level,
            message,
            latitude,
            longitude,
            timestamp
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            level,
            message,
            latitude,
            longitude,
            timestamp
        )
    )

    conn.commit()