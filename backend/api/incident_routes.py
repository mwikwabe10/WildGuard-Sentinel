from fastapi import APIRouter, HTTPException
import sqlite3

from backend.models.incident import create_incident_model
from backend.services.response_service import (
    incident_to_json,
    incidents_to_json
)


router = APIRouter(
    prefix="/incidents",
    tags=["Incidents"]
)


DB_NAME = "wildguard.db"


# ==================================
# CREATE INCIDENT
# POST /incidents/
# ==================================

@router.post("/")
def create_incident(data: dict):

    incident = create_incident_model(data)


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

            incident["incident_type"],

            incident["category"],

            incident["description"],

            incident["latitude"],

            incident["longitude"],

            incident["severity"],

            incident["reported_by"],

            incident["status"],

            incident["created_at"]

        )

    )


    conn.commit()


    incident_id = cursor.lastrowid


    conn.close()


    incident["incident_id"] = incident_id


    return {

        "message": "Incident created",

        "incident": incident

    }



# ==================================
# GET ALL INCIDENTS
# GET /incidents/
# ==================================

@router.get("/")
def get_incidents():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT *
        FROM incidents
        ORDER BY id DESC
        """
    )


    rows = cursor.fetchall()


    conn.close()


    return incidents_to_json(rows)



# ==================================
# GET SINGLE INCIDENT
# GET /incidents/{id}
# ==================================

@router.get("/{incident_id}")
def get_incident(
    incident_id:int
):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT *
        FROM incidents
        WHERE id=?
        """,

        (incident_id,)

    )


    incident = cursor.fetchone()


    conn.close()



    if incident is None:

        raise HTTPException(

            status_code=404,

            detail="Incident not found"

        )


    return incident_to_json(incident)



# ==================================
# UPDATE INCIDENT STATUS
# PUT /incidents/{id}
# ==================================

@router.put("/{incident_id}")
def update_incident(

    incident_id:int,

    status:str

):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()


    cursor.execute(
        """
        UPDATE incidents

        SET status=?

        WHERE id=?

        """,

        (

            status,

            incident_id

        )

    )


    conn.commit()


    updated = cursor.rowcount


    conn.close()



    if updated == 0:

        raise HTTPException(

            status_code=404,

            detail="Incident not found"

        )



    return {

        "message":
        "Incident status updated",

        "status":
        status

    }



# ==================================
# DELETE INCIDENT
# DELETE /incidents/{id}
# ==================================

@router.delete("/{incident_id}")
def delete_incident(

    incident_id:int

):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()



    cursor.execute(
        """
        DELETE FROM incidents

        WHERE id=?

        """,

        (incident_id,)

    )


    conn.commit()


    deleted = cursor.rowcount


    conn.close()



    if deleted == 0:

        raise HTTPException(

            status_code=404,

            detail="Incident not found"

        )



    return {

        "message":
        "Incident deleted"

    }