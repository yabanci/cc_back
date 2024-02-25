class Courier:
    def __init__(self, name: str, location: Location) -> None:
        self.name = name
        self.location = location


class Location:
    def __init__(self, longtitude: float, latitude: float) -> None:
        self.longtitude = longtitude
        self.latitude = latitude
