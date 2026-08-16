from pyspark.sql import functions as F

def validate_sales(df):
    return {
        "row_count": df.count(),
        "null_transaction_id": df.filter(F.col("transaction_id").isNull()).count(),
        "invalid_quantity": df.filter(F.col("quantity") <= 0).count(),
        "duplicate_transaction_id": (
            df.groupBy("transaction_id").count().filter(F.col("count") > 1).count()
        ),
    }

def assert_sales_quality(df):
    metrics = validate_sales(df)
    if metrics["null_transaction_id"] > 0:
        raise ValueError("Sales data contains null transaction_id values.")
    if metrics["invalid_quantity"] > 0:
        raise ValueError("Sales data contains non-positive quantities.")
    if metrics["duplicate_transaction_id"] > 0:
        raise ValueError("Sales data contains duplicate transaction IDs.")
    return metrics
