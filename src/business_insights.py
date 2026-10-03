import pandas as pd


# LOAD DATA
df = pd.read_csv("data/train_featured.csv")



# BASIC BUSINESS METRICS
total_customers = df["Customer_ID"].nunique()

churned_customers = (df["Churn"] == 1).sum()

active_customers = (df["Churn"] == 0).sum()

churn_rate = churned_customers / total_customers * 100

monthly_revenue_at_risk = (
    df.loc[df["Churn"] == 1, "Monthly_Spending"].sum()
)


print("\n" + "=" * 60)
print("CUSTOMER CHURN BUSINESS INSIGHTS")
print("=" * 60)


print("\n1. OVERALL CUSTOMER STATUS")
print("-" * 40)

print(f"Total Customers       : {total_customers:,}")
print(f"Active Customers      : {active_customers:,}")
print(f"Churned Customers     : {churned_customers:,}")
print(f"Overall Churn Rate    : {churn_rate:.2f}%")
print(f"Monthly Revenue Risk  : {monthly_revenue_at_risk:,.2f}")



# SUBSCRIPTION ANALYSIS
subscription_analysis = (
    df.groupby("Subscription_Type")
    .agg(
        Customers=("Customer_ID", "count"),
        Churned=("Churn", "sum"),
        Avg_Spending=("Monthly_Spending", "mean")
    )
)

subscription_analysis["Churn_Rate"] = (
    subscription_analysis["Churned"]
    / subscription_analysis["Customers"]
    * 100
)

subscription_analysis = subscription_analysis.sort_values(
    "Churn_Rate",
    ascending=False
)


print("\n\n2. SUBSCRIPTION ANALYSIS")
print("-" * 40)

print(
    subscription_analysis.round(2)
)



# LOCATION ANALYSIS
location_analysis = (
    df.groupby("Location")
    .agg(
        Customers=("Customer_ID", "count"),
        Churned=("Churn", "sum")
    )
)

location_analysis["Churn_Rate"] = (
    location_analysis["Churned"]
    / location_analysis["Customers"]
    * 100
)

location_analysis = location_analysis.sort_values(
    "Churn_Rate",
    ascending=False
)


print("\n\n3. LOCATION ANALYSIS")
print("-" * 40)

print(
    location_analysis.round(2)
)



# TENURE ANALYSIS
tenure_analysis = (
    df.groupby("Tenure_Category", observed=False)
    .agg(
        Customers=("Customer_ID", "count"),
        Churned=("Churn", "sum")
    )
)

tenure_analysis["Churn_Rate"] = (
    tenure_analysis["Churned"]
    / tenure_analysis["Customers"]
    * 100
)


print("\n\n4. TENURE ANALYSIS")
print("-" * 40)

print(
    tenure_analysis.round(2)
)



# SATISFACTION ANALYSIS
satisfaction_analysis = (
    df.groupby("Satisfaction_Level", observed=False)
    .agg(
        Customers=("Customer_ID", "count"),
        Churned=("Churn", "sum")
    )
)

satisfaction_analysis["Churn_Rate"] = (
    satisfaction_analysis["Churned"]
    / satisfaction_analysis["Customers"]
    * 100
)


print("\n\n5. SATISFACTION ANALYSIS")
print("-" * 40)

print(
    satisfaction_analysis.round(2)
)



# REVENUE AT RISK
revenue_risk = (
    df[df["Churn"] == 1]
    .groupby("Subscription_Type")["Monthly_Spending"]
    .sum()
    .sort_values(ascending=False)
)


print("\n\n6. REVENUE AT RISK BY SUBSCRIPTION")
print("-" * 40)

print(
    revenue_risk.round(2)
)



# HIGH-VALUE CHURNED CUSTOMERS
high_value_churned = (
    df[
        (df["Churn"] == 1) &
        (df["Customer_Value"] >= 5000)
    ]
    .sort_values(
        "Customer_Value",
        ascending=False
    )
)


print("\n\n7. HIGH-VALUE CHURNED CUSTOMERS")
print("-" * 40)

print(
    high_value_churned[
        [
            "Customer_ID",
            "Subscription_Type",
            "Monthly_Spending",
            "Account_Age_Months",
            "Customer_Value",
            "Satisfaction_Score"
        ]
    ].head(10)
)



# SUPPORT ANALYSIS
support_analysis = (
    df.groupby("Churn")[
        [
            "Support_Calls",
            "Complaint_Tickets",
            "Satisfaction_Score"
        ]
    ]
    .mean()
)


print("\n\n8. SUPPORT & SATISFACTION COMPARISON")
print("-" * 40)

print(
    support_analysis.round(2)
)



# FINAL OBSERVATIONS
print("\n\n9. KEY BUSINESS OBSERVATIONS")
print("-" * 40)

highest_subscription = subscription_analysis.index[0]
highest_subscription_rate = subscription_analysis.iloc[0]["Churn_Rate"]

highest_location = location_analysis.index[0]
highest_location_rate = location_analysis.iloc[0]["Churn_Rate"]

highest_tenure = tenure_analysis["Churn_Rate"].idxmax()
highest_tenure_rate = tenure_analysis["Churn_Rate"].max()

highest_satisfaction = satisfaction_analysis["Churn_Rate"].idxmax()
highest_satisfaction_rate = satisfaction_analysis["Churn_Rate"].max()


print(
    f"• Highest observed subscription churn: "
    f"{highest_subscription} ({highest_subscription_rate:.2f}%)"
)

print(
    f"• Highest observed location churn: "
    f"{highest_location} ({highest_location_rate:.2f}%)"
)

print(
    f"• Highest observed tenure-category churn: "
    f"{highest_tenure} ({highest_tenure_rate:.2f}%)"
)

print(
    f"• Highest observed satisfaction-category churn: "
    f"{highest_satisfaction} ({highest_satisfaction_rate:.2f}%)"
)

print(
    f"• Total monthly revenue associated with churned customers: "
    f"{monthly_revenue_at_risk:,.2f}"
)

print("\n" + "=" * 60)
print("BUSINESS INSIGHT ANALYSIS COMPLETED")
print("=" * 60)