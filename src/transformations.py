from pyspark.sql import functions as F

def clean_sales(df):
    return (
        df.dropDuplicates(["transaction_id"])
          .filter(F.col("quantity") > 0)
          .withColumn("sale_date", F.to_date("sale_date"))
          .withColumn("unit_price", F.col("unit_price").cast("double"))
          .withColumn(
              "total_amount",
              F.col("quantity") * F.col("unit_price")
          )
    )

def build_gold_daily_sales(sales_df):
    return (
        sales_df.groupBy("store_id", "sale_date")
        .agg(
            F.sum("total_amount").alias("total_sales"),
            F.sum("quantity").alias("total_quantity"),
            F.countDistinct("customer_code").alias("unique_customers"),
            F.countDistinct("transaction_id").alias("transaction_count")
        )
    )

def build_gold_product_performance(sales_df, products_df):
    return (
        sales_df.join(products_df, "product_code", "left")
        .groupBy("product_code", "product_name", "category")
        .agg(
            F.sum("total_amount").alias("total_sales"),
            F.sum("quantity").alias("units_sold")
        )
    )
