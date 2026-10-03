import pandas as pd


# Load Dataset
file_path = "data/train.csv"
df = pd.read_csv(file_path)



# Dataset Shape


print("\n===== DATASET SHAPE =====")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])



# Column Names


print("\n===== COLUMN NAMES =====")
for column in df.columns:
    print(column)



# First 5 Records


print("\n===== FIRST 5 RECORDS =====")
print(df.head())



# Data Types


print("\n===== DATA TYPES =====")
print(df.dtypes)



# Missing Values


print("\n===== MISSING VALUES =====")
missing_values = df.isnull().sum()
print(missing_values)



# Duplicate Records

print("\n===== DUPLICATES =====")
print("Duplicate rows:", df.duplicated().sum())



# Unique Values

print("\n===== UNIQUE VALUES =====")

for column in df.columns:
    print(f"{column}: {df[column].nunique()}")



# Statistical Summary


print("\n===== STATISTICAL SUMMARY =====")
print(df.describe())



# Churn Distribution

print("\n===== CHURN DISTRIBUTION =====")
print(df["Churn"].value_counts())

print("\n===== CHURN PERCENTAGE =====")
print(df["Churn"].value_counts(normalize=True) * 100)
print("\n===== VALUE RANGES =====")

numeric_columns = [
    "Age",
    "Account_Age_Months",
    "Monthly_Spending",
    "Total_Usage_Hours",
    "Support_Calls",
    "Late_Payments",
    "Streaming_Usage",
    "Discount_Used",
    "Satisfaction_Score",
    "Complaint_Tickets",
    "Promo_Opted_In",
    "Churn"
]

for column in numeric_columns:
    print(
        f"{column}: "
        f"Min={df[column].min()}, "
        f"Max={df[column].max()}"
    )


print("\n===== CATEGORICAL VALUES =====")

categorical_columns = [
    "Gender",
    "Location",
    "Subscription_Type",
    "Last_Interaction_Type"
]

for column in categorical_columns:
    print(f"\n{column}:")
    print(df[column].value_counts())