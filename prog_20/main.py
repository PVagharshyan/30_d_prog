from guests import Guest
from reservations import Reservation
from rooms import Room, StandardRoom, DeluxeRoom

if __name__ == "__main__":
    standard_room1 = StandardRoom(101, 89.99, ["TV", "WiFi"])
    deluxe_room1 = DeluxeRoom(201, 149.99, ["Jacuzzi", "Balcony"])

    guest1 = Guest("Alice", "alice@example.com")

    reservation1 = guest1.book_room(standard_room1, "2023-12-15", "2023-12-17")
    reservation1.add_feedback("Great stay!")

    guest2 = Guest("Bob", "bob@example.com")
    reservation2 = guest2.book_room(deluxe_room1, "2023-12-20", "2023-12-25")
    reservation2.add_feedback("Wonderful experience!")

    print(f"{guest1.name}'s Reservation History:")
    for reservation in guest1.view_reservation_history():
        print(f"Room Number: {reservation.room.room_number}")
        print(f"Check-in: {reservation.checkin_date}, Check-out: {reservation.checkout_date}")
        if reservation.feedback:
            print(f"Feedback: {reservation.feedback}")
        print()

    print(f"{guest2.name}'s Reservation History:")
    for reservation in guest2.view_reservation_history():
        print(f"Room Number: {reservation.room.room_number}")
        print(f"Check-in: {reservation.checkin_date}, Check-out: {reservation.checkout_date}")
        if reservation.feedback:
            print(f"Feedback: {reservation.feedback}")
        print()
