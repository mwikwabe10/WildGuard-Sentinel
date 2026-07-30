from fastapi import FastAPI, UploadFile, File
from pathlib import Path
from datetime import datetime
import shutil
import sqlite3

from backend.api.map_routes import router as map_router
from backend.api.camera_routes import router as camera_router
from backend.api.user_routes import router as user_router
from backend.api.protected_area_routes import router as protected_area_router
from backend.api.incident_routes import router as incident_router

from backend.data_store import detections, alerts

from backend.services.megadetector_service import detect_objects
from backend.services.alert_service import create_alert

from backend.database import init_db

from backend.services.database_service import (
    save_detection,
    save_alert
)


# -----------------------------------
# Initialize Database
# -----------------------------------

init_db()


# -----------------------------------
# FastAPI Application
# -----------------------------------

app = FastAPI(
    title="WildGuard Sentinel",
    version="0.4.0"
)


# -----------------------------------
# Register API Routers
# -----------------------------------

app.include_router(map_router)

app.include_router(camera_router)

app.include_router(user_router)

app.include_router(protected_area_router)

app.include_router(incident_router)



# -----------------------------------
# Upload Directory
# -----------------------------------

UPLOAD_DIR = Path(
    "data/uploads"
)

UPLOAD_DIR.mkdir(
    parents=True,
    exist_ok=True
)



# -----------------------------------
# Root
# -----------------------------------

@app.get("/")
def root():

    return {

        "status": "running",

        "system": "WildGuard Sentinel",

        "version": "0.4.0"

    }



# -----------------------------------
# Health Check
# -----------------------------------

@app.get("/health")
def health():

    return {

        "healthy": True

    }



# -----------------------------------
# Upload Image + AI Detection
# -----------------------------------

@app.post("/upload-image")
async def upload_image(
    file: UploadFile = File(...)
):

    file_path = UPLOAD_DIR / file.filename


    with open(file_path, "wb") as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )


    results = detect_objects(
        file_path
    )


    generated_alerts = []


    for detection in results:


        timestamp = detection.get(
            "timestamp",
            datetime.now().isoformat()
        )


        latitude = detection.get(
            "latitude",
            0.0
        )


        longitude = detection.get(
            "longitude",
            0.0
        )


        alert = create_alert(
            detection["category"],
            detection["confidence"]
        )


        generated_alerts.append(alert)

        alerts.append(alert)



        detection_record = {

            "filename": file.filename,

            "category": detection["category"],

            "confidence": detection["confidence"],

            "latitude": latitude,

            "longitude": longitude,

            "timestamp": timestamp

        }


        detections.append(
            detection_record
        )



        save_detection(

            file.filename,

            detection["category"],

            detection["confidence"],

            latitude,

            longitude,

            timestamp

        )



        save_alert(

            alert["alert_level"],

            alert["message"],

            latitude,

            longitude,

            timestamp

        )



    return {

        "filename": file.filename,

        "detections": results,

        "alerts": generated_alerts

    }



# -----------------------------------
# Simulation Test
# -----------------------------------

@app.post("/simulate-detection")
def simulate_detection():


    timestamp = datetime.now().isoformat()


    latitude = -1.4061

    longitude = 35.1439



    detection = {


        "filename": "camera_001.jpg",

        "category": "human",

        "confidence": 0.97,

        "latitude": latitude,

        "longitude": longitude,

        "timestamp": timestamp

    }



    detections.append(
        detection
    )



    save_detection(

        detection["filename"],

        detection["category"],

        detection["confidence"],

        latitude,

        longitude,

        timestamp

    )



    alert = create_alert(

        detection["category"],

        detection["confidence"]

    )



    alerts.append(alert)



    save_alert(

        alert["alert_level"],

        alert["message"],

        latitude,

        longitude,

        timestamp

    )



    return {

        "detection": detection,

        "alert": alert

    }



# -----------------------------------
# Memory APIs
# -----------------------------------

@app.get("/detections")
def get_detections():

    return detections



@app.get("/alerts")
def get_alerts():

    return alerts



# -----------------------------------
# Database APIs
# -----------------------------------

@app.get("/database/detections")
def database_detections():

    conn = sqlite3.connect(
        "wildguard.db"
    )

    cursor = conn.cursor()


    cursor.execute(
        "SELECT * FROM detections"
    )


    rows = cursor.fetchall()


    conn.close()


    return rows



@app.get("/database/alerts")
def database_alerts():

    conn = sqlite3.connect(
        "wildguard.db"
    )

    cursor = conn.cursor()


    cursor.execute(
        "SELECT * FROM alerts"
    )


    rows = cursor.fetchall()


    conn.close()


    return rows