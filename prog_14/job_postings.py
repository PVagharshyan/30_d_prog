from job_seekers import JobSeeker
import utility
import copy

class JobPosting:
    def __init__(self, title: str, description: str, salary: float):
        self.title = title
        self.description = description
        self.salary = salary
        self._applicants = []

    @utility.type_checking(JobSeeker)
    def apply(self, job_seeker: JobSeeker) -> bool:
        if job_seeker not in self._applicants:
            self._applicants.append(job_seeker)
            return True
        return False

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    @utility.type_checking(str)
    def title(self, value: str):
        self._title = value

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    @utility.type_checking(str)
    def description(self, value: str):
        self._description = value

    @property
    def salary(self) -> float:
        return self._salary

    @salary.setter
    @utility.type_checking((int, float))
    def salary(self, value: (int, float)):
        self._salary = float(value)

    @property
    def applicants(self):
        return copy.deepcopy(self._applicants)

class FullTimeJob(JobPosting):
    def __init__(self, title: str, description: str, salary: float):
        super().__init__(title, description, salary)

class PartTimeJob(JobPosting):
    def __init__(self, title: str, description: str, hourly_rate: float, hours_per_week: int):
        self.hourly_rate = hourly_rate
        self.hours_per_week = hours_per_week
        super().__init__(title, description, hourly_rate * hours_per_week)

    @property
    def hourly_rate(self) -> float:
        return self._hourly_rate

    @hourly_rate.setter
    @utility.type_checking((int, float))
    def hourly_rate(self, value: float):
        self._hourly_rate = float(value)

    @property
    def hours_per_week(self) -> int:
        return self._hours_per_week

    @hours_per_week.setter
    @utility.type_checking(int)
    def hours_per_week(self, value: int):
        self._hours_per_week = value
