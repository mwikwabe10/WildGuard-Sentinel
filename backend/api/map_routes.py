from fastapi import APIRouter
import sqlite3

router = APIRouter()

DB_NAME = "wildguard.db"


@router.get("/map/detections")
def map_detections():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT 
            filename,
            category,
            confidence,
            latitude,
            longitude,
            timestamp
        FROM detections
        """
    )

    rows = cursor.fetchall()

    conn.close()


    features = []

    for row in rows:

        features.append({

            "type": "Feature",

            "geometry": {
                "type": "Point",
                "coordinates": [
                    row[4],   # longitude
                    row[3]    # latitude
                ]
            },

            "properties": {

                "filename": row[0],

                "category": row[1],

                "confidence": row[2],

                "timestamp": row[5]

            }

        })


    return {

        "type": "FeatureCollection",

        "features": features

    }



@router.get("/map/alerts")
def map_alerts():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT
            alert_level,
            message,
            latitude,
            longitude,
            timestamp
        FROM alerts
        """
    )


    rows = cursor.fetchall()

    conn.close()


    features = []


    for row in rows:

        features.append({

            "type": "Feature",

            "geometry": {

                "type": "Point",

                "coordinates": [
                    row[3],
                    row[2]
                ]

            },

            "properties": {

                "alert_level": row[0],

                "message": row[1],

                "timestamp": row[4]

            }

        })


    return {

        "type": "FeatureCollection",

        "features": features

    }