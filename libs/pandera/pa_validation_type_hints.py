from datetime import datetime
from pathlib import Path

import pandas as pd
import pandera as pa
from pandera.typing import DataFrame
from pandera.typing import Series


class OutputSchema(pa.DataFrameModel):
    """Schema for retail products dataset."""

    InvoiceNo: Series[str]
    StockCode: Series[str] = pa.Field(nullable=True)
    Description: Series[str] = pa.Field(nullable=True)
    Quantity: Series[int]
    InvoiceDate: Series[object]
    UnitPrice: Series[float]
    CustomerID: Series[float] = pa.Field(nullable=True)
    Country: Series[str]


@pa.check_types(lazy=True)
def retrieve_retail_products(path: Path) -> DataFrame[OutputSchema]:
    return pd.read_csv(path)


def main() -> None:
    dataset_path = Path().absolute() / "libs" / "pandera" / "datasets"

    products_df = retrieve_retail_products(dataset_path / "online_retail.csv")

    print(products_df)


if __name__ == "__main__":
    main()
