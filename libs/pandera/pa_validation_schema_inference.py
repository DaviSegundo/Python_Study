from pathlib import Path

import pandas as pd
import pandera as pa
from altered_schema import schema


def retrieve_retail_products(path: Path) -> pd.DataFrame:
    return pd.read_csv(path)


def main() -> None:
    dataset_path = Path().absolute() / "libs" / "pandera" / "datasets"

    products_df = retrieve_retail_products(dataset_path / "online_retail.csv")

    products_inferred_schema = pa.infer_schema(products_df)
    with open("inferred_schema.py", "w", encoding="utf-8") as file:
        file.write(products_inferred_schema.to_script())

    try:
        schema.validate(products_df, lazy=True)
    except pa.errors.SchemaErrors as err:
        print(err)

    print(products_df)


if __name__ == "__main__":
    main()
