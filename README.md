# Azure Retail Data Engineering Pipeline

## 🚀 End-to-End Azure Data Engineering Portfolio Project

An end-to-end retail data engineering project demonstrating a modern Azure data platform using **Azure Data Factory, ADLS Gen2, Azure Databricks, PySpark, Delta Lake, SQL and GitHub**.

The project implements a **Medallion Architecture (Bronze → Silver → Gold)** with incremental processing, Delta Lake MERGE/upsert, SCD Type 2, data quality validation and production-oriented pipeline design.

> **Portfolio project:** This repository is designed for learning, demonstration and interview preparation. Azure paths and configuration values are placeholders and should be replaced before deployment to a real environment.

---

## 🏗️ Architecture

```text
                    RETAIL DATA SOURCES
                 CSV / JSON / Transactions
                           |
                           v
                +-----------------------+
                |   Azure Data Factory  |
                |     Orchestration     |
                +-----------+-----------+
                            |
                            v
                +-----------------------+
                |      ADLS Gen2       |
                |     Raw / Landing     |
                +-----------+-----------+
                            |
                            v
                +-----------------------+
                |   Azure Databricks    |
                |     PySpark / Spark   |
                +-----------+-----------+
                            |
             +--------------+--------------+
             |              |              |
             v              v              v
        +---------+    +---------+    +---------+
        | BRONZE  | -> | SILVER  | -> |  GOLD   |
        | Raw     |    | Cleaned  |    | Business|
        | Delta   |    | Enriched |    | Metrics |
        +---------+    +---------+    +---------+
             |              |              |
             |              |              |
             |         SCD Type 2           |
             |         Data Quality          |
             |         Delta MERGE           |
             |                                |
             +---------------+----------------+
                             |
                             v
                  +-----------------------+
                  | Synapse / Power BI    |
                  | Reporting & Analytics |
                  +-----------------------+

                         GitHub
                           |
                    Source Control
                           |
                    CI/CD Automation
