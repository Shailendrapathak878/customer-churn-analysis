import pandas as pd


# LOAD DATA
df = pd.read_csv("data/train_featured.csv")
print("Dataset Shape:", df.shape)

#  TOTAL CUSTOMERS
total_customers = df["Customer_ID"].nunique()

# CHURNED CUSTOMERS
churned_customers = (df["Churn"] == 1).sum()

#  ACTIVE CUSTOMERS
active_customers = (df["Churn"] == 0).sum()



# OVERALL CHURN RATE
churn_rate = (churned_customers / total_customers) * 100



# AVERAGE MONTHLY SPENDING
avg_monthly_spending = df["Monthly_Spending"].mean()



# AVERAGE CUSTOMER VALUE
avg_customer_value = df["Customer_Value"].mean()



# AVERAGE ACCOUNT AGE
avg_account_age = df["Account_Age_Months"].mean()

# AVERAGE SUPPORT CALLS
avg_support_calls = df["Support_Calls"].mean()



# AVERAGE SATISFACTION SCORE
avg_satisfaction = df["Satisfaction_Score"].mean()

#  REVENUE AT RISK
revenue_at_risk = df.loc[
    df["Churn"] == 1,
    "Monthly_Spending"
].sum()



# DISPLAY KPIs
print("CUSTOMER CHURN BUSINESS KPIs")


print(f"Total Customers          : {total_customers:,}")
print(f"Churned Customers        : {churned_customers:,}")
print(f"Active Customers         : {active_customers:,}")
print(f"Overall Churn Rate       : {churn_rate:.2f}%")
print(f"Avg Monthly Spending     : {avg_monthly_spending:.2f}")
print(f"Avg Customer Value       : {avg_customer_value:.2f}")
print(f"Avg Account Age          : {avg_account_age:.2f} months")
print(f"Avg Support Calls        : {avg_support_calls:.2f}")
print(f"Avg Satisfaction Score   : {avg_satisfaction:.2f}")
print(f"Monthly Revenue at Risk  : {revenue_at_risk:.2f}")

