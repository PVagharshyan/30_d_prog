from typing import List
from job_postings import FullTimeJob, PartTimeJob, JobPosting
from job_seekers import JobSeeker
from job_search_platform import JobSearchSite, JobSearchPlatform
from companies import Company
from info import Info

if __name__ == "__main__":
    job_search_site = JobSearchSite()
    google = Company("Google", "contact@google.com")
    microsoft = Company("Microsoft", "contact@microsoft.com")

    job_seeker1 = JobSeeker("John Doe", "john@example.com", "Resume: John")
    job_seeker2 = JobSeeker("Alice Smith", "alice@example.com", "Resume: Alice")
    job_seeker3 = JobSeeker("Bob Johnson", "bob@example.com", "Resume: Bob")

    job_search_site.job_postings.extend([google.create_job_posting("Software", "Develop software", 100000),
                                         microsoft.create_job_posting("Data Scientist", "Analyze data", 90000),
                                         FullTimeJob("AI Researcher", "AI research position", 110000),
                                         PartTimeJob("Part-time", "Part-time development job", 30, 20)])
    for job in job_search_site.search_jobs("Software"):
        if job_search_site.apply_for_job(job, job_seeker1):
            print(f"{job_seeker1.name} applied for this job.")
        if job_search_site.apply_for_job(job, job_seeker2):
            print(f"{job_seeker2.name} applied for this job.")

    for job in job_search_site.search_jobs("Part-time"):
        print(f"Job Title: {job.title}, Salary: {job.salary}")
        if job_search_site.apply_for_job(job, job_seeker3):
            print(f"{job_seeker3.name} applied for this job.")

    for posting in google.job_postings:
        applicants = google.review_applications(posting)
        print(f"Applicants for {posting.title} at {google.name}:")
        for applicant in applicants:
            print(applicant.name)
