# Data-Quality-Checker-System
Data Quality Checker System – Built an automated data validation tool using Python and Pandas to detect missing values, duplicates, schema mismatches, and data inconsistencies, improving data reliability for analytics workflows.
Overview

The Data Quality Checker System is a Python-based project designed to validate and improve dataset quality before analysis. It identifies common data issues such as missing values, duplicate records, incorrect data types, and schema mismatches, ensuring reliable and accurate analytics.

🎯 **Problem Statement**

Poor data quality leads to incorrect insights, faulty dashboards, and bad business decisions. This project automates data validation checks to ensure datasets are clean, consistent, and analysis-ready.

🛠️** Tech Stack**

Python
Pandas
NumPy

**CSV / Excel datasets**

📂 Project Structure
Data-Quality-Checker/
├── data/
│   └── sample_data.csv
├── scripts/
│   └── data_quality_checker.py
├── output/
│   └── quality_report.txt
└── README.md

**🔍 Quality Checks Performed**

Missing value detection
Duplicate record identification
Data type validation
Schema consistency check
Outlier detection (basic)
Summary quality report generation

**⚙️ How It Works**

Loads the dataset using Pandas
Performs automated validation checks
Flags data quality issues
Generates a structured quality report
Helps analysts clean data before analysis
