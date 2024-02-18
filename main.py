import json
import csv
from employee_service_data import EmployeeServiceData
from employer import Employer
from job_seeker import JobSeeker

def main():
    data_module = EmployeeServiceData()

    employer = Employer("RaiymbekDil")
    employer.add_employee(data_module)

    job_seeker = JobSeeker()
    job_seeker.find_employee(data_module)

    with open("employee_service_data.json", "w") as json_file:
        json.dump([vars(e) for e in data_module.employees], json_file)

    with open("employee_service_data.csv", "w", newline="") as csv_file:
        fieldnames = ["name", "position", "hourly_rate", "availability"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for employee in data_module.employees:
            writer.writerow(vars(employee))

if __name__ == "__main__":
    main()
