from fastapi import APIRouter
import sqlite3


router = APIRouter(
    tags=["Statistics"]
)


DB_NAME = "wildguard.db"



@router.get("/statistics")
def get_statistics():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()


    # Total detections

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM detections
        """
    )

    total_detections = cursor.fetchone()[0]



    # Detection categories

    cursor.execute(
        """
        SELECT category, COUNT(*)
        FROM detections
        GROUP BY category
        """
    )


    detections_by_category = {}

    for category, count in cursor.fetchall():

        detections_by_category[category] = count



    # Alert levels

    cursor.execute(
        """
        SELECT alert_level, COUNT(*)
        FROM alerts
        GROUP BY alert_level
        """
    )


    alerts_by_level = {}


    for level, count in cursor.fetchall():

        alerts_by_level[level] = count



    # Recent detections

    cursor.execute(
        """
        SELECT *
        FROM detections
        ORDER BY id DESC
        LIMIT 10
        """
    )


    recent = cursor.fetchall()



    conn.close()



    return {

        "total_detections": total_detections,

        "detections_by_category": detections_by_category,

        "alerts_by_level": alerts_by_level,

        "recent_detections": recent

    }