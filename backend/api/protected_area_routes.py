from fastapi import APIRouter
import sqlite3


router = APIRouter(
    prefix="/protected-areas",
    tags=["Protected Areas"]
)


DB_NAME = "wildguard.db"



@router.post("/")
def create_area(data: dict):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()


    cursor.execute(
        """
        INSERT INTO protected_areas
        (
            name,
            latitude,
            longitude,
            radius
        )
        VALUES (?,?,?,?)
        """,
        (
            data["name"],
            data["latitude"],
            data["longitude"],
            data["radius"]
        )
    )


    conn.commit()
    conn.close()


    return {
        "message": "Protected area created"
    }



@router.get("/")
def get_areas():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()


    cursor.execute(
        "SELECT * FROM protected_areas"
    )


    rows = cursor.fetchall()

    conn.close()


    return rows