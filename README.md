# Azure Retail Data Engineering Pipeline

An end-to-end portfolio project demonstrating a modern Azure data engineering workflow using Azure Data Factory, Azure Data Lake Storage Gen2, Azure Databricks, PySpark, Delta Lake, SQL and GitHub.

> **Portfolio project:** This repository is designed for learning and demonstration. Replace placeholder Azure paths and configuration values before deploying to a real environment.

## Architecture

```text
Retail CSV/JSON Sources
        |
        v
Azure Data Factory
        |
        v
ADLS Gen2 - Raw
        |
        v
Azure Databricks / PySpark
        |
        +--> Bronze - Raw Delta
        |
        +--> Silver - Cleansed & Enriched
        |
        +--> Gold - Business Aggregations
        |
        v
Synapse / Power BI
```

## Business Scenario

A retail organization receives customer, product and sales transactions from multiple sources. The pipeline ingests the raw data, removes duplicates and invalid records, enriches transactions with product attributes, and produces reporting-ready datasets.

## Technologies

- Azure Data Factory
- Azure Data Lake Storage Gen2
- Azure Databricks
- PySpark / Apache Spark
- Delta Lake
- SQL
- Python
- Git / GitHub

## Repository Structure

```text
notebooks/     Databricks/Jupyter notebooks
src/           Reusable PySpark modules
sql/           Reporting and analytical SQL
tests/         Unit tests
config/        Environment configuration template
sample_data/   Small synthetic sample datasets
docs/          Architecture/documentation
```

## Data Layers

### Bronze
Raw source data with ingestion metadata.

### Silver
Cleansed and standardized data:
- duplicate removal
- data type normalization
- invalid quantity filtering
- calculated `total_amount`
- product enrichment

### Gold
Business-ready aggregates:
- daily store sales
- product performance
- customer sales analysis

## Local Practice

Install dependencies:

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate

pip install -r requirements.txt
```

The notebooks are intended for PySpark/Databricks. For Azure Databricks, update the storage paths to ADLS Gen2 locations.

## Git Workflow

```bash
git clone <your-repository-url>
cd azure-retail-data-engineering

git checkout -b feature/retail-pipeline

git add .
git commit -m "Added retail bronze silver gold pipeline"

git push -u origin feature/retail-pipeline
```

Then create a Pull Request in GitHub and merge after review.

## Production Enhancements

For a production implementation, consider adding:
- Azure Key Vault for secrets
- Managed Identity / service principals
- ADF parameterized pipelines
- Incremental processing using watermarks
- Delta MERGE / upsert logic
- Data quality framework
- Structured logging and monitoring
- CI/CD with GitHub Actions or Azure DevOps
- Unity Catalog and catalog-level governance
- Spark performance tuning
- Automated tests

## Portfolio Notes

This project demonstrates practical skills in:
- Medallion architecture
- PySpark transformations
- Delta Lake
- Data quality
- Modular Python
- SQL analytics
- Git/GitHub source control
- Azure data platform design
