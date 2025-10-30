import csv
from room import Room
def save(rooms):
    with open("bookings_final_state.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["room_no", "building", "capacity", "booked_hours"])
        for room in rooms.values():
            booked_str = ";".join(str(h) for h in sorted(room.booked_hours))
            writer.writerow([room.room_no, room.building, room.capacity, booked_str])

def load():
    rooms = {}
    try:
        with open("bookings_final_state.csv", newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                booked_hours = [int(h) for h in row["booked_hours"].split(';') if h] if row["booked_hours"] else []
                rooms[row["room_no"]] = Room(
                    room_no=row["room_no"],
                    building=row["building"],
                    capacity=int(row["capacity"]),
                    booked_hours=booked_hours,
                )
    except FileNotFoundError:
        pass
    return rooms
