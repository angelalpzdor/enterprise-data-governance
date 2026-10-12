
import pandas as pd
import pytest

from src.governance.data_loader import load_dataset


def test_load_valid_dataset(tmp_path):
    """Verify that a valid CSV file is loaded correctly."""
    file_path = tmp_path / "employees.csv"

    expected = pd.DataFrame({
        "employee_id": [1, 2, 3],
        "department": ["IT", "HR", "Finance"]
    })
    expected.to_csv(file_path, index=False)

    result = load_dataset(file_path)

    pd.testing.assert_frame_equal(result, expected)


def test_load_missing_file(tmp_path):
    """Verify that missing files raise an error."""
    file_path = tmp_path / "missing.csv"

    with pytest.raises(FileNotFoundError):
        load_dataset(file_path)


def test_load_empty_file(tmp_path):
    """Verify that an empty CSV raises an error."""
    file_path = tmp_path / "empty.csv"
    file_path.write_text("", encoding="utf-8")

    with pytest.raises(ValueError, match="empty"):
        load_dataset(file_path)


def test_load_header_only_file(tmp_path):
    """Verify that a CSV without records is rejected."""
    file_path = tmp_path / "headers.csv"
    file_path.write_text(
        "employee_id,department\n",
        encoding="utf-8"
    )

    with pytest.raises(ValueError, match="no records"):
        load_dataset(file_path)


def test_load_unsupported_format(tmp_path):
    """Verify that unsupported extensions are rejected."""
    file_path = tmp_path / "employees.txt"
    file_path.write_text("employee_id\n1\n", encoding="utf-8")

    with pytest.raises(ValueError, match="Unsupported"):
        load_dataset(file_path)


def test_load_malformed_csv(tmp_path):
    """Verify that malformed CSV records are rejected."""
    file_path = tmp_path / "malformed.csv"
    file_path.write_text(
        "employee_id,department\n"
        "1,IT\n"
        "2,HR,unexpected_value\n",
        encoding="utf-8"
    )

    with pytest.raises(ValueError, match="malformed"):
        load_dataset(file_path)
