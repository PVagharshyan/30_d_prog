from info import Info
from job_postings import JobPosting
from typing import List
import copy
import utility

class Company:
    def __init__(self, name: str, contact_info: str):
        self.name = name
        self.contact_info = contact_info
        self._job_postings = []

    @utility.type_checking(str, str, int)
    def create_job_posting(self, title: str, description: str, salary: (float, int)) -> JobPosting:
        job_posting = JobPosting(title, description, salary)
        self._job_postings.append(job_posting)
        return job_posting

    @utility.type_checking(JobPosting)
    def review_applications(self, job_posting: JobPosting) -> List['JobSeeker']:
        return job_posting.applicants

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    @utility.type_checking(str)
    def name(self, value: str):
        self._name = value

    @property
    def contact_info(self) -> str:
        return self._contact_info

    @contact_info.setter
    @utility.type_checking(str)
    def contact_info(self, value: str):
        self._contact_info = value

    @property
    def job_postings(self):
        return copy.deepcopy(self._job_postings)
