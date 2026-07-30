from datetime import datetime


class Camera:

    def __init__(
        self,
        camera_id,
        name,
        latitude,
        longitude,
        location,
        status="ACTIVE"
    ):

        self.camera_id = camera_id

        self.name = name

        self.latitude = latitude

        self.longitude = longitude

        self.location = location

        self.status = status

        self.created_at = datetime.now().isoformat()



    def to_dict(self):

        return {

            "camera_id": self.camera_id,

            "name": self.name,

            "latitude": self.latitude,

            "longitude": self.longitude,

            "location": self.location,

            "status": self.status,

            "created_at": self.created_at

        }