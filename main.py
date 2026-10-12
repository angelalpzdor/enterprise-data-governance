from pathlib import Path

from src.governance.catalog import generate_catalog
from src.governance.data_loader import load_dataset


def main():
    """Load a dataset and export its technical catalog."""
    input_path = Path("data/sample/employees.csv")
    output_path = Path("reports/data_catalog.csv")

    print("=== ENTERPRISE DATA GOVERNANCE ===")

    try:
        dataset = load_dataset(input_path)
    except (FileNotFoundError, ValueError) as error:
        print(f"Error: {error}")
        return

    print(f"Records: {len(dataset):,}")
    print(f"Columns: {len(dataset.columns)}")

    catalog = generate_catalog(dataset)

    print("\n=== DATA CATALOG ===")
    print(catalog.to_string(index=False))

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    catalog.to_csv(output_path, index=False)

    print(f"\nCatalog exported to: {output_path}")


if __name__ == "__main__":
    main()
