# Enterprise Data Governance

**A Python-based toolkit for data cataloging, data quality assessment, and responsible data management.**

## Overview

Enterprise Data Governance is an open-source portfolio project designed to explore practical approaches to enterprise data governance.

The project aims to help organizations understand their datasets, document technical metadata, evaluate data quality, and progressively incorporate privacy and AI governance practices.

It is designed to be adaptable to different industries rather than focusing on one particular business sector.

## Current Features

- Automated technical data catalog generation.
- CSV dataset loading and basic structural validation.
- Column-level metadata extraction.
- Missing-value and unique-value statistics.
- CSV report generation.
- Reproducible synthetic employee dataset containing 10,000 records.
- Automated tests using pytest.

## Technology Stack

- Python
- Pandas
- Pytest
- Git and GitHub

## Project Structure

```text
enterprise-data-governance/
├── data/
│   └── sample/
│       └── employees.csv
├── scripts/
│   └── generate_sample_data.py
├── src/
│   └── governance/
│       ├── catalog.py
│       └── data_loader.py
├── tests/
│   ├── test_catalog.py
│   └── test_data_loader.py
├── reports/
├── main.py
├── requirements.txt
└── README.md
```

## Getting Started

Clone the repository:

```bash
git clone https://github.com/angelalpzdor/enterprise-data-governance.git
cd enterprise-data-governance
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Generate the synthetic dataset:

```bash
python scripts/generate_sample_data.py
```

Run the application:

```bash
python main.py
```

The technical data catalog is exported to:

`reports/data_catalog.csv`

## Running Tests

```bash
python -m pytest -q
```

## Planned Features

- Configurable data quality rules.
- Data profiling and validation.
- Personal data classification.
- GDPR-oriented compliance documentation.
- AI system inventory and risk assessment.
- Interactive governance dashboard.
- Audit reports and recommendations.

## Data Privacy

All included sample records are synthetically generated.

The project is intended for educational and portfolio purposes. It does not provide legal advice or certify compliance with the GDPR or EU AI Act.

## Project Status

**Active development — Initial Data Catalog module.**

## Author

Ángela López Dorta