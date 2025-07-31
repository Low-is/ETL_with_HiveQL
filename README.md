# ETL Project with HiveQL: Simulated Variant Data Warehouse
Simulate ingestion of genomic variant data from CSV files --> transform and standardize --> load into Hive tables --> run analytical queries using HiveQL

## Project Summary
This project demonstrates an end-to-end ETL workflow for genomic variant data using Hive on Hadoop, simulating a real-world bioinformatics data engineering scenario.

Variant interpretation refers to the process of analyzing DNA sequence changes (variants) to determine their potential clinical significance. According to the standards and guidelines established by the American College of Medical Genetics and Genomics (ACMG), variants are classified into five categories: pathogenic, likely pathogenic, uncertain significance, likely benign, and benign ([RICHARDS et al., 2015](https://www.acmg.net/docs/Standards_Guidelines_for_the_Interpretation_of_Sequence_Variants.pdf)). 

ETL stands for Extract, Transform, Load, which is a process used to move data from various sources into centralized system, like a data warehouse or data lake, in a usable format. 
- Extract:
    - Pull data from multiple sources: databases, flat files (CSV, JSON), APIs, cloud storage, etc.
    - Sources can be structured (SQL databases), semi-structured (XML, JSON), or unstructured (text, images).
- Transform:
    - Clean, enrich, and convert data into a consistent format.
    - Typical transformations include:
        1. Removing duplicates
        2. Standardizing data/time formats
        3. Joining datasets
        4. Filtering irrelevant rows
        5. Calculating new metrics or columns
- Load:
    - Move the transformed data into a destination system, often a data warehouse like Snowflake, BigQuery, or Amazon Redshift.
    - Data can be loaded:
        1. All at once (batch load)
        2. Incrementally (only new/updated data)




Using a Dockerized big data environment (based on the big-data-europe/docker-hive stack), the following is performed:

1. Simulated genomic variant data for 1000+ variants across 200 samples and multiple genes.

2. Uploaded the data into HDFS (Hadoop Distributed File System).

3. Created an external Hive table to query the data using HiveQL.

4. Ran analytical queries (e.g., variant counts per gene) to simulate downstream interpretation workflows.

Key Technologies being used:
1. Docker + [Docker Compose](https://github.com/big-data-europe/docker-hive/blob/master/docker-compose.yml) – for running Hadoop and Hive services.
2. Apache Hive – for scalable SQL-based analysis of tabular variant data.
3. Hadoop (HDFS) – for distributed storage of large datasets.
4. Python (Pandas) – to simulate realistic variant data.


Quick workflow:
Download docker-compose.yml file (refer to above link) from Big Data Europe's GitHub repo. 

Open your command prompt or Windows Powershell:
```
# Move into directory containing docker-compes.yml file (Windows PowerShell example)
PS C:\Users\RANDOLPHL cd path\to\file
```

```
# Once inside directory where docker-compose.yml file lives, type the following to start the stack:
# This will start:
# PostgreSQL as Hive Metastore DB
# Hive Metastore service
# Hiveserver2 service
docker-compose up -d
```

```
# From local machine, copy variant file inside Hive container:
hdfs cp C:\Users\RANDOLPHL\ETL_project\variants_simulated.csv hive-server:/variants_simulated.csv
```

```
# Access the Hive CLI (Beeline)
docker exec -it hive-server /bin/bash
```


```
# Once inside the container, create directory for files into container's HDFS (Hadoop Distribution File System):
hdfs dfs -mkdir -p /user/hive/warehouse/variants
```


```
# Load files into HDFS from inside the container
hdfs dfs -put /variants_simulated.csv /user/hive/warehouse/variants/
```


```
# Start Beeline (Hive CLI):
beeline -u jdbc://localhost:1000
```

```
# After starting the Beeline (Hive CLI), the following prompt will appear as:
# 0:jdbchive2://localhost:10000>
```
