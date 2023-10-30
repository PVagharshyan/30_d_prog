from typing import List, Optional, Type
from rooms import Room
import utility

class Guest:
    ...

class Reservation:
    def __init__(self, guest: Guest, room: Room, checkin_date: str, checkout_date: str):
        self.guest = guest
        self.room = room
        self.checkin_date = checkin_date
        self.checkout_date = checkout_date
        self._feedback: Optional[str] = None

    @property
    def guest(self) -> Type[Guest]:
        return self._guest

    @guest.setter
    @utility.type_checking(Guest)
    def guest(self, guest: Type[Guest]):
        self._guest = guest

    @property
    def room(self) -> Type[Room]:
        return self._room

    @room.setter
    @utility.type_checking(Room)
    def room(self, room: Type[Room]):
        self._room = room

    @property
    def checkin_date(self) -> str:
        return self._checkin_date

    @checkin_date.setter
    @utility.type_checking(str)
    def checkin_date(self, checkin_date: str):
        self._checkin_date = checkin_date

    @property
    def checkout_date(self) -> str:
        return self._checkout_date

    @checkout_date.setter
    @utility.type_checking(str)
    def checkout_date(self, checkout_date: str):
        self._checkout_date = checkout_date

    @property
    def feedback(self) -> Optional[str]:
        return self._feedback

    @feedback.setter
    @utility.type_checking(str)
    def feedback(self, feedback: Optional[str]):
        self._feedback = feedback

    @utility.type_checking(str)
    def add_feedback(self, feedback: str):
        self._feedback = feedback
