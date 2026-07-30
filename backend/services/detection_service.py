import sqlite3
from datetime import datetime


DB_NAME = "wildguard.db"


def process_detection(detection):

    category = detection["category"]
    confidence = detection["confidence"]


    # AI rule engine
    if category == "HUMAN" and confidence >= 0.85:


        create_incident_from_detection(detection)



def create_incident_from_detection(detection):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()


    cursor.execute(
        """
        INSERT INTO incidents
        (
            incident_type,
            category,
            description,
            latitude,
            longitude,
            severity,
            reported_by,
            status,
            timestamp
        )

        VALUES (?,?,?,?,?,?,?,?,?)

        """,
        (
            "POACHING",
            "WILDLIFE_CRIME",
            "Human detected near protected zone",
            detection["latitude"],
            detection["longitude"],
            "CRITICAL",
            detection.get("filename","AI_CAMERA"),
            "OPEN",
            datetime.now().isoformat()
        )
    )


    conn.commit()

    conn.close()


    return {
        "message":"Incident generated from AI detection"
    }