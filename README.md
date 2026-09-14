# Data Integration Pipeline

An end-to-end Python ETL pipeline that demonstrates data ingestion, validation, transformation, cleansing, and preparation of curated data for downstream analytics.

## Overview

This project simulates a real-world data integration workflow in which raw customer data may contain duplicates, missing identifiers, inconsistent formatting, and invalid values.

The pipeline automatically:

- Extracts raw data from a CSV source
- Validates required fields and schema
- Detects duplicate and missing customer IDs
- Cleans and standardizes customer information
- Handles invalid date values
- Removes duplicate and unusable records
- Creates derived fields for downstream use
- Loads the curated dataset into a processed output file
- Logs pipeline execution and data-quality results

## Architecture

Raw CSV Data  
↓  
Data Ingestion  
↓  
Data Validation & Quality Checks  
↓  
Data Transformation & Cleansing  
↓  
Curated Dataset  
↓  
Analytics / Reporting

## Technologies

- Python
- Pandas
- CSV
- Data Validation
- ETL
- Logging

## Project Structure

    data-integration-pipeline/
    ├── data/
    │   └── raw/
    │       └── customer_data.csv
    ├── pipeline.py
    ├── requirements.txt
    └── README.md

The pipeline automatically creates:

    data/processed/customer_data_clean.csv

when it is executed.

## Data Quality Checks

The sample dataset intentionally contains several common data-quality issues, including:

- Duplicate customer IDs
- Missing customer IDs
- Invalid dates
- Inconsistent capitalization
- Extra whitespace
- Inconsistent email formatting

The pipeline detects or corrects these issues before producing the curated dataset.

## How to Run

Install the required dependency:

    pip install -r requirements.txt

Run the pipeline:

    python pipeline.py

The processed dataset will be written to:

    data/processed/customer_data_clean.csv

## Skills Demonstrated

- ETL pipeline development
- Data ingestion and transformation
- Data cleansing and validation
- Data quality monitoring
- Python automation
- Pandas data processing
- Error handling
- Logging
- Reproducible data workflows

## Future Enhancements

- Load curated data into PostgreSQL or SQL Server
- Add automated unit and data-quality tests
- Add workflow orchestration with Apache Airflow
- Implement SQL transformations with dbt
- Add CI/CD validation using GitHub Actions
- Integrate cloud storage such as AWS S3
