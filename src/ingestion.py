from pyspark.sql import functions as F

def add_ingestion_metadata(df):
    return df.withColumn("ingestion_timestamp", F.current_timestamp())

def read_csv(spark, path):
    return (
        spark.read
        .option("header", "true")
        .option("inferSchema", "true")
        .csv(path)
    )
