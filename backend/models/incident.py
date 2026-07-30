from datetime import datetime


class Incident:

    def __init__(
        self,
        incident_id=None,
        incident_type=None,
        category=None,
        description=None,
        latitude=0.0,
        longitude=0.0,
        severity="LOW",
        reported_by="SYSTEM",
        status="OPEN"
    ):

        self.incident_id = incident_id

        self.incident_type = incident_type

        self.category = category

        self.description = description

        self.latitude = latitude

        self.longitude = longitude

        self.severity = severity

        self.reported_by = reported_by

        self.status = status

        self.created_at = datetime.now().isoformat()



    def to_dict(self):

        return {

            "incident_id": self.incident_id,

            "incident_type": self.incident_type,

            "category": self.category,

            "description": self.description,

            "latitude": self.latitude,

            "longitude": self.longitude,

            "severity": self.severity,

            "reported_by": self.reported_by,

            "status": self.status,

            "created_at": self.created_at

        }



def create_incident_model(data):

    incident = Incident(

        incident_type=data.get(
            "incident_type",
            "UNKNOWN"
        ),

        category=data.get(
            "category",
            "GENERAL"
        ),

        description=data.get(
            "description",
            ""
        ),

        latitude=data.get(
            "latitude",
            0.0
        ),

        longitude=data.get(
            "longitude",
            0.0
        ),

        severity=data.get(
            "severity",
            "LOW"
        ),

        reported_by=data.get(
            "reported_by",
            "SYSTEM"
        )

    )


    return incident.to_dict()