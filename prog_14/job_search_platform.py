from abc import ABC, abstractmethod
from typing import List
from job_postings import JobPosting
from job_seekers import JobSeeker
import utility
import copy

class JobSearchPlatform(ABC):
    @abstractmethod
    def search_jobs(self, keyword: str) -> List['JobPosting']:
        pass

    @abstractmethod
    def apply_for_job(self, job_posting: 'JobPosting') -> bool:
        pass

class JobSearchSite(JobSearchPlatform):
    def __init__(self):
        self._job_postings = []

    @utility.type_checking(str)
    def search_jobs(self, keyword: str) -> List[JobPosting]:
        return [job for job in self.job_postings if keyword == job.title or keyword == job.description]

    @utility.type_checking(JobPosting, JobSeeker)
    def apply_for_job(self, job_posting: JobPosting, job_seeker: JobSeeker) -> bool:
        return job_posting.apply(job_seeker)

    @property
    def job_postings(self) -> List[JobPosting]:
        return self._job_postings
