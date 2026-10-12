
import csv
import random
from datetime import date, datetime, timedelta
from pathlib import Path


RECORD_COUNT = 10_000
RANDOM_SEED = 42
OUTPUT_FILE = Path("data/sample/employees.csv")

COUNTRIES = {
    "Spain": ["Madrid", "Barcelona", "Las Palmas"],
    "Germany": ["Berlin", "Munich", "Hamburg"],
    "France": ["Paris", "Lyon", "Marseille"],
    "Italy": ["Rome", "Milan", "Turin"],
    "Netherlands": ["Amsterdam", "Rotterdam"],
    "Portugal": ["Lisbon", "Porto"],
    "Ireland": ["Dublin", "Cork"],
    "Belgium": ["Brussels", "Antwerp"],
}

DEPARTMENTS = {
    "IT": ["Software Engineer", "Data Engineer", "IT Analyst"],
    "HR": ["HR Specialist", "Recruiter", "HR Manager"],
    "Finance": ["Accountant", "Financial Analyst"],
    "Marketing": ["Marketing Analyst", "SEO Specialist"],
    "Sales": ["Sales Executive", "Account Manager"],
    "Operations": ["Operations Analyst", "Coordinator"],
    "Legal": ["Legal Assistant", "Compliance Analyst"],
    "Data Governance": ["Data Steward", "Governance Analyst"],
}

FIRST_NAMES = [
    "Emma", "Olivia", "Sophia", "Isabella", "Mia",
    "Charlotte", "Amelia", "Lucas", "Noah", "Liam",
    "James", "Oliver", "Daniel", "Ethan", "Alexander",
]

LAST_NAMES = [
    "Smith", "Johnson", "Brown", "Davis", "Wilson",
    "Taylor", "Anderson", "Thomas", "Martin", "Garcia",
    "Lopez", "Miller", "Clark", "Walker", "Hall",
]


def random_date(start, end):
    """Return a random date between two dates."""
    days = (end - start).days
    return start + timedelta(days=random.randint(0, days))


def generate_employee(employee_id):
    """Generate one synthetic employee record."""
    first_name = random.choice(FIRST_NAMES)
    last_name = random.choice(LAST_NAMES)

    department = random.choice(list(DEPARTMENTS))
    job_title = random.choice(DEPARTMENTS[department])

    country = random.choice(list(COUNTRIES))
    city = random.choice(COUNTRIES[country])

    birth_date = random_date(
        date(1960, 1, 1),
        date(2003, 12, 31)
    )

    minimum_hire_date = max(
        date(2015, 1, 1),
        birth_date + timedelta(days=18 * 365 + 5)
    )

    hire_date = random_date(
        minimum_hire_date,
        date(2026, 9, 30)
    )

    salary = random.randint(24_000, 95_000)

    email = (
        f"{first_name.lower()}."
        f"{last_name.lower()}."
        f"{employee_id}@example.com"
    )

    return {
        "employee_id": employee_id,
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "department": department,
        "job_title": job_title,
        "country": country,
        "city": city,
        "employment_type": random.choice(
            ["Full-time", "Part-time", "Contract"]
        ),
        "salary_eur": salary,
        "hire_date": hire_date.isoformat(),
        "birth_date": birth_date.isoformat(),
        "manager_id": (
            random.randint(1, employee_id - 1)
            if employee_id > 1 else ""
        ),
        "performance_score": random.randint(1, 5),
        "status": random.choice(["Active", "Inactive"]),
        "last_updated": random_date(
            hire_date,
            date(2026, 10, 1)
        ).isoformat(),
    }


def introduce_quality_issues(records):
    """
    Introduce intentional data quality issues.

    These anomalies allow the governance toolkit
    to evaluate missing values, invalid values,
    duplicates, and inconsistent records.
    """
    for record in records:
        if random.random() < 0.05:
            record["email"] = ""

        if random.random() < 0.03:
            record["salary_eur"] = ""

        if random.random() < 0.02:
            record["department"] = ""

        if random.random() < 0.01:
            record["performance_score"] = 8

        if random.random() < 0.01:
            record["salary_eur"] = -1000

        if random.random() < 0.01:
            record["email"] = "invalid-email"

    # Deliberately duplicate five complete records.
    # Replace existing rows to keep the dataset
    # at exactly 10,000 records.
    for index in range(5):
        records[-(index + 1)] = records[index].copy()

    return records


def main():
    """Generate and export a synthetic employee dataset."""
    random.seed(RANDOM_SEED)

    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    records = [
        generate_employee(employee_id)
        for employee_id in range(1, RECORD_COUNT + 1)
    ]

    records = introduce_quality_issues(records)

    with OUTPUT_FILE.open(
        "w",
        newline="",
        encoding="utf-8"
    ) as file:
        writer = csv.DictWriter(
            file,
            fieldnames=list(records[0].keys())
        )

        writer.writeheader()
        writer.writerows(records)

    print("=== SYNTHETIC DATA GENERATION ===")
    print(f"Records generated: {len(records):,}")
    print(f"Columns: {len(records[0])}")
    print(f"Output file: {OUTPUT_FILE}")
    print("Data generation completed successfully.")


if __name__ == "__main__":
    main()
