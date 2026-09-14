"""
Data Integration Pipeline
-------------------------
A simple ETL pipeline demonstrating:
1. Data ingestion
2. Data validation
3. Data cleansing and transformation
4. Data quality monitoring
5. Loading curated data for downstream analytics
"""

import pandas as pd
import logging
from pathlib import Path


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

RAW_DATA = Path("data/raw/customer_data.csv")
OUTPUT_DATA = Path("data/processed/customer_data_clean.csv")


def extract_data(file_path):
    """Read raw customer data from a CSV source."""
    logging.info("Extracting data from %s", file_path)

    df = pd.read_csv(file_path)

    logging.info("Extracted %s records", len(df))
    return df


def validate_data(df):
    """Perform basic data-quality checks."""

    required_columns = [
        "customer_id",
        "first_name",
        "last_name",
        "email",
        "signup_date",
        "status"
    ]

    missing_columns = [
        column for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    duplicate_count = df.duplicated(
        subset=["customer_id"]
    ).sum()

    missing_id_count = df["customer_id"].isna().sum()

    logging.info(
        "Data quality check: %s duplicate customer IDs",
        duplicate_count
    )

    logging.info(
        "Data quality check: %s missing customer IDs",
        missing_id_count
    )

    return True


def transform_data(df):
    """Clean and standardize incoming data."""

    logging.info("Transforming data")

    df = df.copy()

    # Remove duplicate customers
    df = df.drop_duplicates(
        subset=["customer_id"],
        keep="last"
    )

    # Remove records without a customer ID
    df = df.dropna(subset=["customer_id"])

    # Convert customer IDs to integers after removing missing values
    df["customer_id"] = df["customer_id"].astype(int)

    # Standardize text fields
    df["first_name"] = (
        df["first_name"]
        .fillna("")
        .str.strip()
        .str.title()
    )

    df["last_name"] = (
        df["last_name"]
        .fillna("")
        .str.strip()
        .str.title()
    )

    df["email"] = (
        df["email"]
        .fillna("")
        .str.strip()
        .str.lower()
    )

    df["status"] = (
        df["status"]
        .fillna("unknown")
        .str.strip()
        .str.lower()
    )

    # Convert signup date into a consistent format
    df["signup_date"] = pd.to_datetime(
        df["signup_date"],
        errors="coerce"
    )

    # Add a useful derived field
    df["full_name"] = (
        df["first_name"] + " " + df["last_name"]
    ).str.strip()

    logging.info(
        "Transformation complete: %s records remain",
        len(df)
    )

    return df


def load_data(df, output_path):
    """Write curated data for downstream analytics."""

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    df.to_csv(
        output_path,
        index=False
    )

    logging.info(
        "Processed data written to %s",
        output_path
    )


def run_pipeline():
    """Execute the complete ETL workflow."""

    logging.info("Starting data integration pipeline")

    df = extract_data(RAW_DATA)

    validate_data(df)

    clean_df = transform_data(df)

    load_data(clean_df, OUTPUT_DATA)

    logging.info("Pipeline completed successfully")


if __name__ == "__main__":
    run_pipeline()
