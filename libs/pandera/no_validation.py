from pathlib import Path

import pandas as pd


def retrieve_retail_products(path: Path) -> pd.DataFrame:
    return pd.read_csv(path)


def main() -> None:
    dataset_path = Path().absolute() / "libs" / "pandera" / "datasets"

    products_df = retrieve_retail_products(dataset_path / "online_retail.csv")
    print(products_df)


if __name__ == "__main__":
    main()
