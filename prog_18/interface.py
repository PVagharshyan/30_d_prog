from abc import ABC, abstractmethod

class HealthCareOperation(ABC):
    @abstractmethod
    def execute(self):
        pass

class AppointmentType(ABC):
    @abstractmethod
    def get_type(self) -> str:
        pass
