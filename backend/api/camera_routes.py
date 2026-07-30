from fastapi import APIRouter
import sqlite3


router = APIRouter(
    prefix="/cameras",
    tags=["Cameras"]
)


DB_NAME = "wildguard.db"



@router.post("/")
def create_camera(data: dict):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()


    cursor.execute(
        """
        INSERT INTO cameras
        (
            camera_id,
            name,
            latitude,
            longitude,
            location,
            status
        )
        VALUES (?,?,?,?,?,?)
        """,
        (
            data["camera_id"],
            data["name"],
            data["latitude"],
            data["longitude"],
            data["location"],
            data.get("status", "ACTIVE")
        )
    )


    conn.commit()
    conn.close()


    return {
        "message": "Camera registered",
        "camera": data
    }



@router.get("/")
def get_cameras():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()


    cursor.execute(
        "SELECT * FROM cameras"
    )


    rows = cursor.fetchall()

    conn.close()


    return rows