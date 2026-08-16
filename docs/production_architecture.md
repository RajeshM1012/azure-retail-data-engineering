# Production-Oriented Architecture

Source Files -> Azure Data Factory -> ADLS Gen2 Raw -> Azure Databricks -> Bronze/Silver/Gold Delta -> Synapse/Power BI

ADF also reads a control-table watermark and updates it after successful Databricks processing.

## Incremental Processing
Only records newer than the last successful watermark are processed. In production, store the watermark in a control table rather than hard-coding it.

## SCD Type 2
Customer history uses `effective_from`, `effective_to`, and `is_current`.

## Data Quality
Checks include null transaction IDs, non-positive quantities, duplicate transaction IDs, and row-count metrics.

## Security
Never commit passwords, tokens, connection strings, SAS tokens, or cloud access keys. Use Managed Identity, Key Vault, and RBAC in a real deployment.
