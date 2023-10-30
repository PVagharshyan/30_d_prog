from patients import Patient
from doctors import Doctor, Appointment as Appointment_p
from appointment_type import AppointmentType
from typing import *
import utility

class Appointment(Appointment_p):
    def __init__(self, patient: Patient, doctor: Doctor, appointment_time: str, appointment_type: AppointmentType):
        self.patient = patient
        self.doctor = doctor
        self.appointment_time = appointment_time
        self.appointment_type = appointment_type

    @property
    def patient(self) -> Type[Patient]:
        return self._patient

    @patient.setter
    @utility.type_checking(Patient)
    def patient(self, patient: Type[Patient]):
        self._patient = patient

    @property
    def doctor(self) -> Type[Doctor]:
        return self._doctor

    @doctor.setter
    @utility.type_checking(Doctor)
    def doctor(self, doctor: Type[Doctor]):
        self._doctor = doctor

    @property
    def appointment_time(self) -> str:
        return self._appointment_time

    @appointment_time.setter
    @utility.type_checking(str)
    def appointment_time(self, appointment_time: str):
        self._appointment_time = appointment_time

    @property
    def appointment_type(self) -> Type[AppointmentType]:
        return self._appointment_type

    @appointment_type.setter
    @utility.type_checking(AppointmentType)
    def appointment_type(self, appointment_type: Type[AppointmentType]):
        self._appointment_type = appointment_type
