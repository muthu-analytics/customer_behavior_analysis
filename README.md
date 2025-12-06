# 📊 Customer Shopping Behavior – End-to-End Data Analytics Project

## **1. Overview**
This project demonstrates a complete data analytics workflow using Python, SQL, and Power BI.  
The goal is to analyze customer shopping behavior, identify patterns, and derive actionable business insights.

The workflow includes:
- **Data Loading**
- **Exploratory Data Analysis (EDA)**
- **Data Cleaning**
- **Feature Engineering**
- **SQL-Based Analysis**
- **Power BI Dashboard Creation**
- **Final Reporting and Gamma Presentation**

This project showcases practical skills relevant for **Data Analyst** and **Business Analyst** roles.

---

## **2. Dataset**
- **Raw File:** `customer_shopping_behavior.csv`  
- **Processed File:** `updated_customer_trends.csv`  

**Description:**  
Dataset contains detailed customer demographics, purchase patterns, review ratings, category preferences, discount usage, and shipping types.

**Key Columns Include:**
- age, gender  
- item_purchased, category  
- purchase_amount  
- discount_applied, frequency_of_purchases  
- review_rating  
- subscription_status  
- previous_purchases  

---

## **3. Tools & Technologies**

### **Languages & Libraries**
- Python: Pandas, NumPy, SQLAlchemy, PyMySQL  
- SQL: MySQL (compatible with PostgreSQL / SQL Server)

### **Analytics & Visualization**
- Power BI  
- Gamma (for presentations)

### **Environment**
- Jupyter Notebook / VS Code  
- MySQL Workbench  
- GitHub  

---

## **4. Project Workflow**

### **Step 1: Data Loading**
- Loaded the dataset using Pandas  
- Performed structure checks and missing value analysis  

### **Step 2: Exploratory Data Analysis (EDA)**
- Summary statistics  
- Data distribution analysis  
- Category and demographic insights  
- Discount vs. purchase behavior  
- Review rating patterns  

### **Step 3: Data Cleaning**
- Imputed missing `review_rating` using **category-wise median**  
- Standardized column names (snake_case)  
- Renamed technical fields  
- Removed irrelevant column: `promo_code_used`  
- Ensured consistent data formats  

### **Step 4: Feature Engineering**
- **Created Age Groups** (Young Adult, Adult, Middle-aged, Senior)  
- **Converted Frequency-of-Purchases** text into numerical days  
- Validated discount/promo relationships  
- Exported cleaned dataset to CSV  

### **Step 5: SQL Analytics**
Executed SQL queries from:  
📄 `customer_behavior_sql_queries.sql`

Insights include:
- Revenue comparison by gender  
- Discount users who spent above average  
- Top 5 products by average review rating  
- Standard vs Express shipping insights  
- Subscribed vs non-subscribed spending  
- Discount rate per product  
- Customer segmentation: New / Returning / Loyal  
- Top products within each category  
- Repeat buyer subscription likelihood  
- Age-group revenue contribution  

### **Step 6: Power BI Dashboard**
Power BI file: `customer_behaviour.pbix`

Dashboard includes:
- KPI Cards  
- Category & product insights  
- Age-group performance  
- Purchase trends  
- Subscription impact  
- Review & discount trends  
- Interactive filters & slicers  

### **Step 7: Final Reporting**
- Insight summary report  
- Business recommendations  
- Final Gamma presentation  

---

## **5. Key Insights**  
(*Replace these with your actual results.*)

- Middle-aged customers generate the highest revenue.  
- Express shipping users spend more on average.  
- Electronics category has the highest review ratings.  
- Loyal customers contribute the largest revenue share.  
- Discount usage strongly influences purchase frequency.  

---

## **6. Project Structure**
```
|── customer_trends.py
|── customer_behavior_sql_queries.sql
|── customer_behaviour.pbix
|── customer_shopping_behavior.csv
|── updated_customer_trends.csv
|── reports/
|── README.md
```

---

## **7. How to Run This Project**

### **Install Dependencies**
```bash
pip install pandas numpy sqlalchemy pymysql
```

### **Run Python Script**
```bash
python customer_trends.py
```

### **Load SQL Queries**
Import cleaned dataset into MySQL, then run:
```
customer_behavior_sql_queries.sql
```

### **View Power BI Dashboard**
Open:
```
customer_behaviour.pbix
```

### **View Reports**
Open final report & Gamma presentation in the `reports/` folder.

---

## **8. Deliverables**
- ✔ Cleaned and transformed dataset  
- ✔ SQL analytics file  
- ✔ Power BI dashboard  
- ✔ Python data processing script  
- ✔ Final insights report  
- ✔ Gamma presentation  


