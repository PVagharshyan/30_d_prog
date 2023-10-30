from typing import List
from patients import Patient
from doctors import Doctor
from appointments import Appointment
from appointment_type import AppointmentType

class HealthCareSystem:
    def __init__(self):
        self.patients: List[Patient] = []
        self.doctors: List[Doctor] = []

    @utility.type_checking(Patient, Doctor, str, AppointmentType)
    def schedule_appointment(self, patient: Patient, doctor: Doctor, appointment_time: str, appointment_type: AppointmentType):
        appointment = Appointment(patient, doctor, appointment_time, appointment_type)
        doctor.manage_schedule(appointment)
        return appointment

    def view_patient_medical_history(self, patient: Patient) -> List[str]:
        return patient.view_medical_history()
