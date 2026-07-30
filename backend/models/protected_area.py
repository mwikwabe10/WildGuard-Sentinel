class ProtectedArea:


    def __init__(
        self,
        area_id,
        name,
        latitude,
        longitude,
        radius
    ):


        self.area_id = area_id

        self.name = name

        self.latitude = latitude

        self.longitude = longitude

        self.radius = radius



    def to_dict(self):

        return {


            "area_id": self.area_id,

            "name": self.name,

            "latitude": self.latitude,

            "longitude": self.longitude,

            "radius": self.radius

        }