from fastapi import APIRouter
import sqlite3
from datetime import datetime

from backend.models.detection import Detection
from backend.services.detection_service import process_detection


router = APIRouter(
    prefix="/detections",
    tags=["Detections"]
)


DB_NAME="wildguard.db"


@router.post("/")
def create_detection(data: Detection):

    detection = data.dict()


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

        VALUES (?,?,?,?,?,?)
        """,
        (
            detection["filename"],
            detection["category"],
            detection["confidence"],
            detection["latitude"],
            detection["longitude"],
            datetime.now().isoformat()
        )
    )


    conn.commit()

    conn.close()


    # AI rule engine
    process_detection(detection)


    return {
        "message":"Detection processed",
        "detection":detection
    }