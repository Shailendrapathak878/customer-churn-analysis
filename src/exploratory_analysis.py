import pandas as pd

df = pd.read_csv("data/train.csv")

print("\n CHURN BY SUBSCRIPTION TYPE ")
print(pd.crosstab(
    df["Subscription_Type"],
    df["Churn"],
    normalize="index"
) * 100)


print("\n CHURN BY LOCATION ")
print(pd.crosstab(
    df["Location"],
    df["Churn"],
    normalize="index"
) * 100)


print("\n CHURN BY GENDER ")
print(pd.crosstab(
    df["Gender"],
    df["Churn"],
    normalize="index"
) * 100)


print("\n CHURN BY LAST INTERACTION ")
print(pd.crosstab(
    df["Last_Interaction_Type"],
    df["Churn"],
    normalize="index"
) * 100)


print("\n  NUMERICAL COMPARISON ")

numerical_columns = [
    "Age",
    "Account_Age_Months",
    "Monthly_Spending",
    "Total_Usage_Hours",
    "Support_Calls",
    "Late_Payments",
    "Streaming_Usage",
    "Discount_Used",
    "Satisfaction_Score",
    "Complaint_Tickets"
]

print(
    df.groupby("Churn")[numerical_columns].mean().round(2)

)
print("\n CORRELATION WITH CHURN ")

correlation = df.corr(numeric_only=True)["Churn"].sort_values(
    ascending=False
)

print(correlation)

print("\n CHURN RATE BY SUPPORT CALLS ")

support_churn = df.groupby("Support_Calls")["Churn"].mean() * 100
print(support_churn.round(2))


print("\n CHURN RATE BY LATE PAYMENTS ")

late_payment_churn = df.groupby("Late_Payments")["Churn"].mean() * 100
print(late_payment_churn.round(2))


print("\n CHURN RATE BY SATISFACTION SCORE ")

satisfaction_churn = df.groupby("Satisfaction_Score")["Churn"].mean() * 100
print(satisfaction_churn.round(2))


print("\n CHURN RATE BY COMPLAINT TICKETS ")

complaint_churn = df.groupby("Complaint_Tickets")["Churn"].mean() * 100
print(complaint_churn.round(2))

print("\n SUPPORT CALLS + COMPLAINTS VS CHURN ")

support_complaint = pd.crosstab(
    [df["Support_Calls"], df["Complaint_Tickets"]],
    df["Churn"],
    normalize="index"
) * 100

print(support_complaint.round(2))

print("\n SUBSCRIPTION + LATE PAYMENTS VS CHURN ")

subscription_payment = pd.crosstab(
    [df["Subscription_Type"], df["Late_Payments"]],
    df["Churn"],
    normalize="index"
) * 100

print(subscription_payment.round(2))