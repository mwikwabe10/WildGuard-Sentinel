from fastapi import APIRouter
import sqlite3


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


DB_NAME = "wildguard.db"



@router.post("/")
def create_user(data: dict):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()


    cursor.execute(
        """
        INSERT INTO users
        (
            name,
            role
        )
        VALUES (?,?)
        """,
        (
            data["name"],
            data["role"]
        )
    )


    conn.commit()
    conn.close()


    return {
        "message": "User created",
        "user": data
    }



@router.get("/")
def get_users():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()


    cursor.execute(
        "SELECT * FROM users"
    )


    rows = cursor.fetchall()

    conn.close()


    return rows