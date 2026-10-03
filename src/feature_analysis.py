import pandas as pd

# Load feature engineered dataset
df = pd.read_csv("data/train_featured.csv")
print("Dataset Shape:", df.shape)



# CHURN BY TENURE CATEGORY
print("\n===== CHURN BY TENURE CATEGORY =====")

tenure_churn = pd.crosstab(
    df["Tenure_Category"],
    df["Churn"],
    normalize="index"
) * 100

print(tenure_churn.round(2))



# CHURN BY SPENDING CATEGORY
print("\n===== CHURN BY SPENDING CATEGORY =====")

spending_churn = pd.crosstab(
    df["Spending_Category"],
    df["Churn"],
    normalize="index"
) * 100

print(spending_churn.round(2))



# CHURN BY PAYMENT RISK
print("\n===== CHURN BY PAYMENT RISK =====")

payment_churn = pd.crosstab(
    df["Payment_Risk"],
    df["Churn"],
    normalize="index"
) * 100

print(payment_churn.round(2))



# CHURN BY SATISFACTION LEVEL
print("\n===== CHURN BY SATISFACTION LEVEL =====")

satisfaction_churn = pd.crosstab(
    df["Satisfaction_Level"],
    df["Churn"],
    normalize="index"
) * 100

print(satisfaction_churn.round(2))



# CHURN BY SUPPORT INTENSITY
print("\n===== CHURN BY SUPPORT INTENSITY =====")

support_churn = pd.crosstab(
    df["Support_Intensity"],
    df["Churn"],
    normalize="index"
) * 100

print(support_churn.round(2))



# CUSTOMER VALUE VS CHURN
print("\n===== CUSTOMER VALUE BY CHURN =====")

customer_value = df.groupby("Churn")["Customer_Value"].mean()

print(customer_value.round(2))



# USAGE INTENSITY VS CHURN


print("\n===== USAGE INTENSITY BY CHURN =====")

usage_intensity = df.groupby("Churn")["Usage_Intensity"].mean()

print(usage_intensity.round(2))