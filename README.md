📊 Customer Shopping Behavior – End-to-End Data Analytics Project
1. Overview

This project demonstrates a complete data analytics workflow using Python, SQL, and Power BI.
The goal is to analyze customer shopping behavior, identify patterns, and derive actionable business insights.

The workflow includes:

Data loading

Exploratory Data Analysis (EDA)

Data cleaning

Feature engineering

SQL-based analysis

Power BI dashboard creation

Final reporting and presentation using Gamma

This project showcases practical skills relevant for Data Analyst and Business Analyst roles.

2. Dataset

Raw File: customer_shopping_behavior.csv

Processed File: updated_customer_trends.csv

Description:
Contains detailed information about customer demographics, purchases, product categories, discounts, review ratings, and purchase frequency.

Key Columns Include:

age, gender

item_purchased, category

purchase_amount

discount_applied, frequency_of_purchases

review_rating

subscription_status

previous_purchases

3. Tools & Technologies
Languages & Libraries

Python: Pandas, NumPy, SQLAlchemy, PyMySQL

SQL: MySQL (compatible with PostgreSQL / SQL Server)

Analytics & Visualization

Power BI

Gamma (for presentations)

Environment

Jupyter Notebook / VS Code

MySQL Workbench

GitHub

4. Project Workflow
Step 1: Data Loading

Loaded the dataset using Pandas.

Checked structure, data types, and missing values.

Step 2: Exploratory Data Analysis (EDA)

Summary statistics

Missing value inspection

Category/age/gender-level behavior

Purchase amount distribution

Discount & review rating analysis

Step 3: Data Cleaning

Imputed missing review_rating using median grouped by category

Standardized all column names

Renamed technical fields

Removed unnecessary columns (promo_code_used)

Ensured accurate data types

Step 4: Feature Engineering

Created age groups using qcut

Converted purchase frequency text → numerical days

Validated discount/promo fields

Exported cleaned dataset

Step 5: SQL Analytics

Executed SQL queries from:
customer_behavior_sql_queries.sql

SQL insights include:

Gender-based revenue comparison

High spenders who used discounts

Top 5 products by average review rating

Standard vs Express shipping comparison

Subscribed vs non-subscribed average spend

Product discount rate analysis

Customer segmentation: New, Returning, Loyal

Top products per category

Repeat buyer subscription patterns

Revenue contribution by age groups

Step 6: Power BI Dashboard

Used customer_behaviour.pbix to build:

KPI cards

Purchase trends

Category performance

Age group revenue patterns

Subscription impact

Discounts & review rating insights

Interactive slicers and filters

Step 7: Final Reporting

Insight summary report

Business recommendations

Final presentation created using Gamma
