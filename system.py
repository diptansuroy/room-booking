from room import Room, RoomExistsError, RoomNotFoundError, RoomAlreadyBookedError

class RoomBookingSystem:
    def __init__(self, loaded_rooms=None):
        self.rooms = loaded_rooms if loaded_rooms else {}

    def add(self, room_no, building, capacity):
        if room_no in self.rooms:
            raise RoomExistsError()
        self.rooms[room_no] = Room(room_no, building, capacity)

    def book(self, room_no, hour):
        if room_no not in self.rooms:
            raise RoomNotFoundError()
        self.rooms[room_no].book_hour(hour)

    def search(self, building=None, min_capacity=None, free_hour=None):
        results = []
        for room in self.rooms.values():
            if building and room.building != building:
                continue
            if min_capacity and room.capacity < min_capacity:
                continue
            if free_hour is not None and not room.is_available(free_hour):
                continue
            results.append(room)
        return results

    def view(self, room_no):
        if room_no not in self.rooms:
            raise RoomNotFoundError()
        room = self.rooms[room_no]
        booked_str = ",".join(str(h) for h in sorted(room.booked_hours))
        details = (
            f"\n---- Room Details ----\n"
            f"ID: {room.room_no}\n"
            f"Building: {room.building}\n"
            f"Capacity: {room.capacity}\n"
            f"Booked Hours: [{booked_str if booked_str else ''}]"
        )
        return details
