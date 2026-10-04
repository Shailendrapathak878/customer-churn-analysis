# Customer Churn & Intelligence Dashboard

An end-to-end **Data Analytics and Business Intelligence project** focused on customer churn analysis, customer segmentation, revenue-at-risk analysis, business KPIs, SQL analysis, and interactive Power BI reporting.

---

## 📊 Project Overview

Customer churn is an important business problem for subscription-based organizations because customer loss can directly affect recurring revenue and long-term customer value.

This project analyzes customer-level data to understand churn patterns across:

- Subscription Types
- Locations
- Customer Tenure
- Satisfaction Levels
- Support Activity
- Complaint Behavior
- Payment Behavior
- Customer Spending
- Customer Value

The project follows an end-to-end **Data Analytics workflow**, starting from data inspection and preparation and ending with SQL analysis, business insights, and an interactive Power BI dashboard.

---

## 🎯 Business Problem

The objective of this project is to understand customer churn and identify customer segments associated with higher observed churn and revenue risk.

The analysis focuses on questions such as:

- How many customers have churned?
- What is the overall churn rate?
- Which subscription type has the highest observed churn?
- Which locations have higher observed churn?
- How does customer tenure relate to churn?
- Does satisfaction clearly explain churn?
- How much monthly revenue is associated with churned customers?
- Which churned customers have higher customer value?
- Which customer segments require further retention analysis?

---

## 🎯 Project Objectives

1. Measure the overall customer churn rate.
2. Analyze churn across different customer segments.
3. Perform data quality and validation checks.
4. Prepare customer data for business analysis.
5. Create business-oriented analytical features.
6. Perform exploratory data analysis using Python.
7. Perform structured business analysis using PostgreSQL and SQL.
8. Calculate important customer and revenue KPIs.
9. Identify meaningful observed churn patterns.
10. Build an interactive Power BI dashboard.
11. Convert analytical findings into practical business recommendations.

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Data inspection, preparation, feature engineering and analysis |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| PostgreSQL | Database storage and SQL analysis |
| SQL | Business analysis and customer segmentation |
| Power BI | Interactive dashboard and reporting |
| DAX | KPI calculations and dashboard measures |
| Git | Version control |
| GitHub | Project documentation and portfolio |

---

## 🔄 Project Workflow

```text
Customer Dataset
       ↓
Data Inspection
       ↓
Data Quality Validation
       ↓
Data Cleaning & Preparation
       ↓
Feature Engineering
       ↓
Exploratory Data Analysis
       ↓
PostgreSQL Database
       ↓
SQL Business Analysis
       ↓
Business KPIs
       ↓
Power BI Dashboard
       ↓
Business Insights
       ↓
Business Recommendations

Project Structure
Customer-Churn-Analysis/
│
├── data/
│   └── README.md
│
├── src/
│   ├── data_inspection.py
│   ├── data_cleaning.py
│   ├── feature_engineering.py
│   ├── exploratory_analysis.py
│   ├── feature_analysis.py
│   ├── business_kpis.py
│   ├── business_insights.py
│   └── visualization.py
│
├── sql/
│   └── analysis.sql
│
├── output/
│   └── generated analytical visualizations
│
├── requirements.txt
├── .gitignore
└── README.md

The dataset files are intentionally not included in this public repository. See data/README.md for details.

📦 Dataset
The project uses an 8,000-customer dataset containing customer demographic, subscription, usage, support, satisfaction, payment and churn information.
Dataset Size
- Records: 8,000
- Original Columns: 17
- Engineered Analytical Columns: 24
- Target Variable: Churn
Churn Definition
Churn = 0 → Active / Non-churned customer
Churn = 1 → Churned customer

📋 Original Dataset Features
Feature	Description
Customer_ID	Unique customer identifier
Age	Customer age
Gender	Customer gender
Location	Customer location
Subscription_Type	Customer subscription plan
Account_Age_Months	Customer tenure
Monthly_Spending	Monthly customer spending
Total_Usage_Hours	Total usage hours
Support_Calls	Number of support calls
Late_Payments	Number of late payments
Streaming_Usage	Streaming usage measure
Discount_Used	Discount usage measure
Satisfaction_Score	Customer satisfaction score
Last_Interaction_Type	Most recent interaction type
Complaint_Tickets	Number of complaint tickets
Promo_Opted_In	Promotional participation
Churn	Customer churn indicator


⚙️ Feature Engineering
Additional business-oriented features were created to make customer behavior easier to analyze.
The engineered features include:
- Tenure_Category
- Spending_Category
- Usage_Intensity
- Support_Intensity
- Payment_Risk
- Satisfaction_Level
- Customer_Value
These features are used for segment-level analysis and business interpretation.
🔍 Data Quality & Validation
The dataset was inspected and validated before performing the main analysis.
Validation Check	Result
Total Records	8,000
Missing Values	0
Duplicate Rows	0
Unique Customer IDs	8,000


Churn Distribution
Customer Status	Customers	Percentage
Active	5,495	68.69%
Churned	2,505	31.31%
Total	8,000	100%


📊 Business KPIs
The major project KPIs are:
KPI	Value
Total Customers	8,000
Churned Customers	2,505
Active Customers	5,495
Overall Churn Rate	31.31%
Average Monthly Spending	104.80
Average Customer Value	3,165.31
Average Account Age	30.16 months
Average Support Calls	4.45
Average Satisfaction Score	5.46
Monthly Revenue at Risk	264,401.10


Monthly Revenue at Risk
Monthly Revenue at Risk represents the sum of monthly spending associated with customers who have churned.
It should not be interpreted as lifetime revenue loss.
📈 Key Analytical Findings
Subscription Analysis
Observed churn rates:
Subscription Type	Customers	Churned	Churn Rate
Basic	4,063	1,280	31.50%
Premium	3,120	970	31.09%
Enterprise	817	255	31.21%


Observation
Basic has the highest observed churn rate among the three subscription categories.
Location Analysis
Location	Churn Rate
Florida	32.37%
California	31.81%
Texas	31.57%
New York	31.44%
Illinois	29.43%


Observation
Florida has the highest observed churn rate in the dataset.
Tenure Analysis
Tenure Category	Churn Rate
0–12 Months	30.03%
13–24 Months	31.03%
25–36 Months	32.58%
37–48 Months	32.18%
49–60 Months	30.65%


Observation
The 25–36 month tenure segment has the highest observed churn rate.
Satisfaction Analysis
Satisfaction Level	Churn Rate
Excellent	32.72%
Good	31.71%
Medium	31.60%
Low	29.88%


Observation
The Excellent satisfaction category has a higher observed churn rate than the Low satisfaction category.
Therefore, satisfaction alone does not clearly explain churn in this dataset.
Revenue at Risk by Subscription
Subscription Type	Monthly Revenue at Risk
Basic	135,092.69
Premium	102,980.74
Enterprise	26,327.67


Observation
The Basic subscription segment contributes the largest amount of monthly revenue associated with churned customers.
🗄️ PostgreSQL & SQL Analysis
The customer dataset was imported into PostgreSQL for structured business analysis.
The SQL analysis covers:
- Overall customer KPIs
- Churn analysis
- Subscription analysis
- Location analysis
- Gender analysis
- Last interaction analysis
- Tenure analysis
- Spending analysis
- Payment risk analysis
- Satisfaction analysis
- Support analysis
- Complaint analysis
- Promotional participation
- Revenue at risk
- Revenue risk by subscription
- Revenue risk by location
- Revenue risk by tenure
- High-value churned customers
- High-support churned customers
- Low-satisfaction churned customers
- Customer risk segmentation
- Ranking and comparative analysis
SQL Concepts Used
SELECT
WHERE
GROUP BY
CASE
Aggregate Functions
CTEs
Window Functions
Ranking
Segmentation

The complete SQL analysis is available in:
sql/analysis.sql

🐍 Python Analysis
Python was used as the main analytical layer before and alongside PostgreSQL.
Data Inspection
The project performs:
- Dataset shape validation
- Data type inspection
- Missing-value checks
- Duplicate checks
- Unique customer validation
- Categorical distribution analysis
- Numerical range validation
Data Preparation
The project prepares the customer dataset for analytical use through validation, transformation and feature engineering.
Exploratory Data Analysis
The analysis covers:
- Overall churn distribution
- Churn by subscription type
- Churn by location
- Churn by gender
- Churn by tenure
- Churn by satisfaction
- Churn by support activity
- Churn by complaints
- Payment behavior
- Customer value
- Revenue risk
Visualization
Python was also used to generate analytical visualizations for important customer churn metrics.
📊 Power BI Dashboard
The final dashboard is titled:
CUSTOMER CHURN & INTELLIGENCE DASHBOARD
The Power BI dashboard provides an executive-style view of customer churn and revenue risk.
KPI Cards
The dashboard contains:
- Total Customers
- Churned Customers
- Active Customers
- Churn Rate
- Monthly Revenue at Risk
Interactive Slicers
The dashboard provides filtering through:
- Subscription Type
- Location
- Gender
- Tenure Category
- Satisfaction Level
Main Visualizations
The dashboard includes:
- Churn Rate by Subscription Type
- Churn Rate by Location
- Churn Rate by Tenure
- Monthly Revenue at Risk by Subscription
The dashboard allows users to filter customer segments and investigate churn patterns interactively.
💡 Business Recommendations
1. Monitor Basic Subscribers
Basic customers represent the largest customer segment and have the highest observed subscription-level churn rate.
Retention analysis should therefore give attention to this segment.
2. Investigate Florida
Florida has the highest observed location-level churn rate.
The business can investigate whether there are specific customer experience, service or engagement patterns associated with this segment.
3. Monitor Mid-Tenure Customers
The 25–36 month tenure segment shows the highest observed churn rate.
Customers within this tenure range can be included in targeted retention analysis.
4. Prioritize High-Value Customers
Customer Value can be used to prioritize churned or potentially at-risk customers for deeper business investigation.
5. Track Revenue at Risk
Monthly Revenue at Risk should be monitored as an important management KPI because it represents monthly spending associated with churned customers.
6. Avoid Single-Factor Decisions
The analysis does not show a strong single-variable explanation for churn.
Business teams should therefore consider multiple customer attributes together instead of relying on only satisfaction, support calls, payments or another individual metric.
⚠️ Analytical Interpretation
This project is a descriptive Data Analytics project.
The analysis identifies observed patterns but does not establish causal relationships.
For example:
- A higher churn rate in a particular segment does not prove that the segment characteristic causes churn.
- Higher satisfaction does not necessarily prevent churn.
- Support calls and complaint counts show relatively small and mixed differences between churned and active customers.
- Customer churn should therefore be interpreted using multiple customer characteristics together.
The results represent patterns observed within the available dataset.
📌 Important Project Definitions
Churn Rate
The percentage of customers classified as churned among the total customer base.
Churn Rate =
Churned Customers / Total Customers

Monthly Revenue at Risk
The sum of monthly spending associated with customers who have churned.
Monthly Revenue at Risk =
Sum of Monthly Spending for Churned Customers

This metric represents monthly revenue associated with churned customers and is not equivalent to lifetime revenue loss.
🧰 Project Files
Python Scripts
src/
├── data_inspection.py
├── data_cleaning.py
├── feature_engineering.py
├── exploratory_analysis.py
├── feature_analysis.py
├── business_kpis.py
├── business_insights.py
└── visualization.py

SQL
sql/
└── analysis.sql

Data Documentation
data/
└── README.md

The actual CSV files are intentionally excluded from the public repository.
🔐 Dataset Availability
The dataset used in this project is not included in the public GitHub repository.
The dataset was obtained from a Kaggle competition dataset whose redistribution is subject to the applicable competition rules and licensing terms.
Therefore, the following files are intentionally excluded:
train.csv
test.csv
train_featured.csv

The repository contains the analytical code, SQL queries, documentation and project structure without redistributing the underlying dataset.
For more information, see:
data/README.md

🔒 Data Handling
The repository does not distribute the underlying customer dataset.
Dataset files are excluded through .gitignore:
# Dataset files
data/*.csv

# Python
__pycache__/
*.pyc
.venv/
venv/

# VS Code
.vscode/

# Generated outputs
output/

This keeps the public repository focused on the analytical workflow while preventing accidental redistribution of the dataset.
⚠️ Limitations
The project has the following limitations:
- The analysis is descriptive.
- The dataset does not establish causality.
- Many segment-level churn differences are relatively modest.
- Monthly Revenue at Risk is not lifetime revenue loss.
- Historical time-series data was not available for detailed churn trend analysis.
- The findings represent patterns within the available dataset and should not automatically be generalized to every customer population.
🚀 Future Scope
Possible future improvements include:
- Customer cohort analysis
- Historical churn trend analysis
- Retention tracking
- Customer lifetime value segmentation
- Automated Power BI refresh
- More detailed customer behavior analysis
- CRM and customer-support data integration
- Additional business intelligence metrics
- Advanced predictive analytics as a separate future project
📚 Skills Demonstrated
This project demonstrates practical experience in:
- Data Analytics
- Data Cleaning
- Data Quality Validation
- Exploratory Data Analysis
- Feature Engineering
- Python
- Pandas
- NumPy
- Matplotlib
- SQL
- PostgreSQL
- Business KPI Development
- Customer Segmentation
- Revenue Risk Analysis
- Data Visualization
- Power BI
- DAX
- Business Intelligence
- Data Storytelling
- Business Insights
- Git & GitHub
📈 Project Outcome
The project demonstrates a complete business analytics workflow:
Raw Customer Data
        ↓
Data Quality Validation
        ↓
Data Preparation
        ↓
Feature Engineering
        ↓
Python EDA
        ↓
PostgreSQL & SQL Analysis
        ↓
Business KPIs
        ↓
Power BI Dashboard
        ↓
Business Insights
        ↓
Actionable Recommendations

The final outcome is an interactive Customer Churn & Intelligence Dashboard that helps analyze customer churn patterns, segment performance and monthly revenue associated with churned customers.
👨‍💻 Project Type
Data Analytics / Business Intelligence
This project focuses on descriptive analytics, business intelligence and decision support rather than machine learning-based churn prediction.
⭐ Summary
Customer Churn & Intelligence Dashboard is an end-to-end Data Analytics project combining Python, PostgreSQL, SQL and Power BI to transform customer-level data into business-focused insights.
The project demonstrates how raw customer data can be transformed into:
Clean Data → Analytical Features → SQL Insights → KPIs → Interactive Dashboard → Business Recommendations
```