# Architecture Notes

## Components

1. Azure Data Factory orchestrates ingestion.
2. ADLS Gen2 stores raw and curated data.
3. Azure Databricks executes PySpark transformations.
4. Delta Lake provides ACID tables and reliable processing.
5. Gold datasets are consumed by Synapse or Power BI.
6. GitHub manages source code, notebooks and collaboration.

## Recommended Production Flow

ADF -> ADLS Raw -> Databricks Bronze -> Silver -> Gold -> Reporting

## Security

Use Managed Identity, Azure Key Vault and RBAC. Never commit credentials, connection strings or access keys to GitHub.
