class RoomExistsError(Exception):
    pass

class RoomNotFoundError(Exception):
    pass

class RoomAlreadyBookedError(Exception):
    pass

class Room:
    def __init__(self, room_no, building, capacity, booked_hours=None):
        self.room_no = room_no
        self.building = building
        self.capacity = capacity
        self.booked_hours = set(booked_hours) if booked_hours else set()

    def book_hour(self, hour):
        if hour < 0 or hour > 23:
            raise ValueError("Hour must be between 0 and 23 inclusive.")
        if hour in self.booked_hours:
            raise RoomAlreadyBookedError()
        self.booked_hours.add(hour)

    def is_available(self, hour):
        return hour not in self.booked_hours
