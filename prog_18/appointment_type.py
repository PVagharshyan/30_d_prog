from interface import AppointmentType

class InPersonAppointment(AppointmentType):
    def get_type(self) -> str:
        return "In-person"

class VirtualAppointment(AppointmentType):
    def get_type(self) -> str:
        return "Virtual"
