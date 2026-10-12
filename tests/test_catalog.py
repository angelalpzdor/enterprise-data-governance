
import pandas as pd

from src.governance.catalog import generate_catalog


def test_generate_catalog():
    """Check catalog generation for a basic dataset."""
    dataset = pd.DataFrame({
        "employee_id": [1, 2, 3],
        "department": ["IT", "HR", "IT"],
        "salary": [30000, None, 42000],
    })

    catalog = generate_catalog(dataset)

    assert len(catalog) == 3

    salary = catalog.loc[
        catalog["column_name"] == "salary"
    ].iloc[0]

    assert salary["total_records"] == 3
    assert salary["missing_values"] == 1
    assert salary["unique_values"] == 2


def test_generate_catalog_empty_dataset():
    """Check catalog generation for an empty dataset."""
    dataset = pd.DataFrame({
        "employee_id": pd.Series(dtype="int64"),
        "department": pd.Series(dtype="object"),
    })

    catalog = generate_catalog(dataset)

    assert len(catalog) == 2
    assert (catalog["total_records"] == 0).all()
    assert (catalog["missing_values"] == 0).all()


def test_generate_catalog_all_missing_values():
    """Check a column containing only missing values."""
    dataset = pd.DataFrame({
        "email": [None, None, None]
    })

    catalog = generate_catalog(dataset)

    assert catalog.iloc[0]["missing_values"] == 3
    assert catalog.iloc[0]["unique_values"] == 0
