from typing import List, Optional, Type
from rooms import Room
from reservations import Reservation, Guest as Guest_r
import utility
import copy

class Guest(Guest_r):
    def __init__(self, name: str, contact_info: str):
        self.name = name
        self.contact_info = contact_info
        self._reservation_history: List['Reservation'] = []

    @property
    def name(self):
        return self._name

    @name.setter
    @utility.type_checking(str)
    def name(self, value: str):
        self._name = value

    @property
    def contact_info(self):
        return self._contact_info

    @contact_info.setter
    @utility.type_checking(str)
    def contact_info(self, value: str):
        self._contact_info = value

    @property
    def reservation_history(self):
        return copy.deepcopy(self._reservation_history)

    @utility.type_checking(str, str, Room)
    def search_available_rooms(self, checkin_date: str, checkout_date: str, room_type: Type[Room]) -> List[Type[Room]]:
        pass

    @utility.type_checking(Room, str, str)
    def book_room(self, room: Type[Room], checkin_date: str, checkout_date: str) -> 'Reservation':
        reservation = Reservation(self, room, checkin_date, checkout_date)
        self._reservation_history.append(reservation)
        return reservation

    def view_reservation_history(self) -> List['Reservation']:
        return self.reservation_history

    @utility.type_checking(Reservation, str)
    def leave_feedback(self, reservation: 'Reservation', feedback: str):
        reservation.add_feedback(feedback)
