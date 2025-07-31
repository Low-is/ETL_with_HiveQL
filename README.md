# ETL Project with HiveQL: Simulated Variant Data Warehouse
Simulate ingestion of genomic variant data from CSV files --> transform and standardize --> load into Hive tables --> run analytical queries using HiveQL

This project demonstrates an end-to-end ETL workflow for genomic variant data using Hive on Hadoop, simulating a real-world bioinformatics data engineering scenario.

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
