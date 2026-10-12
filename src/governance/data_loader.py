
from pathlib import Path

import pandas as pd
from pandas.errors import EmptyDataError, ParserError


def load_dataset(file_path):
    """
    Load a CSV dataset and validate its basic structure.

    Args:
        file_path: Path to the CSV file.

    Returns:
        A pandas DataFrame containing the dataset.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file is empty or malformed.
    """
    path = Path(file_path)

    if not path.is_file():
        raise FileNotFoundError(
            f"Dataset not found: {path}"
        )

    if path.suffix.lower() != ".csv":
        raise ValueError(
            "Unsupported file format. Only CSV files are allowed."
        )

    try:
        dataset = pd.read_csv(path, on_bad_lines="error")
    except EmptyDataError as error:
        raise ValueError("The CSV file is empty.") from error
    except ParserError as error:
        raise ValueError("The CSV file is malformed.") from error

    if dataset.empty:
        raise ValueError(
            "The dataset contains no records."
        )

    return dataset
