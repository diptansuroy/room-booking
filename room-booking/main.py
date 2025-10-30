from system import RoomBookingSystem
from room import RoomExistsError, RoomNotFoundError, RoomAlreadyBookedError
from storage import load, save

def main():
    print("Welcome to the Classroom Booking System!\n")
    print("(System loads data from bookings_final_state.csv...)\nRooms loaded successfully.\n")

    loaded_rooms = load()
    system = RoomBookingSystem(loaded_rooms)

    while True:
        print("What would you like to do?")
        print("1. Create a new Room")
        print("2. Find Available Rooms")
        print("3. Book a Room")
        print("4. View a Room's Schedule")
        print("5. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print("\n---- Create a New Room ----")
            room_no = input("Enter Room ID (e.g., NAB101): ").strip()
            building = input("Enter Building Name: ").strip()
            capacity = input("Enter Capacity: ").strip()
            try:
                system.add(room_no, building, int(capacity))
                print(f"Success: Room {room_no} created.\n")
            except RoomExistsError:
                print(f"Error: Room with ID {room_no} already exists.\n")
            except ValueError:
                print("Error: Invalid capacity entered.\n")
        elif choice == "2":
            print("\n---- Find Available Rooms ----")
            building = input("Filter by Building Name (leave blank for none): ").strip()
            building = building if building else None
            min_capacity_input = input("Minimum Capacity (leave blank for none): ").strip()
            min_capacity = int(min_capacity_input) if min_capacity_input else None
            free_hour_input = input("Available at Hour (0-23, leave blank for none): ").strip()
            free_hour = int(free_hour_input) if free_hour_input else None
            matched_rooms = system.search(building, min_capacity, free_hour)
            if not matched_rooms:
                print("No rooms found matching the criteria.\n")
            else:
                print(f"Found {len(matched_rooms)} room(s):")
                for room in matched_rooms:
                    print(f"- {room.room_no}, Building: {room.building}, Capacity: {room.capacity}")
                print()
        elif choice == "3":
            print("\n---- Book a Room ----")
            room_no = input("Enter Room ID to book: ").strip()
            hour_input = input("Enter Hour to book (0-23): ").strip()
            try:
                system.book(room_no, int(hour_input))
                print(f"Success: Room {room_no} has been booked for {hour_input}.\n")
            except RoomNotFoundError:
                print(f"Error: Room with ID {room_no} does not exist.\n")
            except RoomAlreadyBookedError:
                print(f"Error: Time slot {hour_input} is already booked for Room {room_no}.\n")
            except ValueError:
                print("Error: Invalid input.\n")
        elif choice == "4":
            print("\n---- View a Room's Schedule ----")
            room_no = input("Enter Room ID: ").strip()
            try:
                print(system.view(room_no) + "\n")
            except RoomNotFoundError:
                print(f"Error: Room with ID {room_no} does not exist.\n")
        elif choice == "5":
            print("\nSaving data to bookings_final_state.csv...")
            save(system.rooms)
            print("Goodbye!\n")
            break
        else:
            print("Invalid choice. Please try again.\n")
main()
