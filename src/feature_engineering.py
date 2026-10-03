import pandas as pd


# LOAD DATA
df = pd.read_csv("data/train.csv")

print("Original Shape:", df.shape)



# TENURE CATEGORY
df["Tenure_Category"] = pd.cut(
    df["Account_Age_Months"],
    bins=[0, 12, 24, 36, 48, 60],
    labels=["0-12 Months", "13-24 Months", "25-36 Months",
            "37-48 Months", "49-60 Months"]
)



# SPENDING CATEGORY
df["Spending_Category"] = pd.cut(
    df["Monthly_Spending"],
    bins=[0, 50, 100, 150, 200],
    labels=["Low", "Medium", "High", "Very High"]
)



# USAGE INTENSITY
df["Usage_Intensity"] = (
    df["Total_Usage_Hours"] / df["Account_Age_Months"]
).round(2)



# SUPPORT INTENSITY
df["Support_Intensity"] = (
    df["Support_Calls"] + df["Complaint_Tickets"]
)



# PAYMENT RISK
df["Payment_Risk"] = pd.cut(
    df["Late_Payments"],
    bins=[-1, 0, 1, 2, 4],
    labels=["No Late Payment", "Low", "Medium", "High"]
)



# SATISFACTION LEVEL
df["Satisfaction_Level"] = pd.cut(
    df["Satisfaction_Score"],
    bins=[0, 3, 6, 8, 10],
    labels=["Low", "Medium", "Good", "Excellent"]
)



# CUSTOMER VALUE
df["Customer_Value"] = (
    df["Monthly_Spending"] *
    df["Account_Age_Months"]
).round(2)



# DISPLAY RESULTS
print("\n===== NEW FEATURES =====")

new_features = [
    "Tenure_Category",
    "Spending_Category",
    "Usage_Intensity",
    "Support_Intensity",
    "Payment_Risk",
    "Satisfaction_Level",
    "Customer_Value"
]

print(df[new_features].head(10))



# SAVE FEATURE ENGINEERED DATA
df.to_csv("data/train_featured.csv", index=False)

print("\nFeature engineered dataset saved successfully!")
print("Final Shape:", df.shape)#