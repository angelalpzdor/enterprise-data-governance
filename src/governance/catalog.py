
import pandas as pd


def generate_catalog(df):
    """
    Generate a technical data catalog from a DataFrame.

    The catalog provides information about each column,
    including its data type, record count, missing values,
    and unique values.
    """
    catalog = []

    for column in df.columns:
        data = df[column]

        column_info = {
            "column_name": column,
            "data_type": str(data.dtype),
            "total_records": len(data),
            "missing_values": int(data.isna().sum()),
            "unique_values": int(data.nunique()),
        }

        catalog.append(column_info)

    return pd.DataFrame(catalog)
