CREATE EXTERNAL TABLE IF NOT EXISTS variants (
    sample_id STRING,
    gene STRING,
    chromosome STRING,
    variant_type STRING,
    impact STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION '/user/hive/warehouse/variants';
