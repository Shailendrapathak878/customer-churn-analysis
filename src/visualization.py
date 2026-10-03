import pandas as pd
import matplotlib.pyplot as plt
import os


# LOAD DATA
df = pd.read_csv("data/train_featured.csv")

print("Dataset Shape:", df.shape)

os.makedirs("output", exist_ok=True)



# COMMON CHART SETTINGS
plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["axes.spines.top"] = False
plt.rcParams["axes.spines.right"] = False
plt.rcParams["axes.spines.left"] = False
plt.rcParams["axes.spines.bottom"] = False
plt.rcParams["axes.grid"] = True
plt.rcParams["grid.alpha"] = 0.25
plt.rcParams["axes.axisbelow"] = True



#  OVERALL CHURN DISTRIBUTION
churn_counts = df["Churn"].value_counts().sort_index()

labels = ["Active", "Churned"]

fig, ax = plt.subplots(figsize=(9, 6))

bars = ax.bar(
    labels,
    churn_counts.values,
    width=0.55
)

ax.set_title(
    "Customer Churn Distribution",
    fontsize=18,
    fontweight="bold",
    pad=20
)

ax.set_ylabel("Number of Customers", fontsize=11)

ax.grid(axis="y")
ax.grid(axis="x", visible=False)

for bar, value in zip(bars, churn_counts.values):

    percentage = value / len(df) * 100

    ax.text(
        bar.get_x() + bar.get_width() / 2,
        value + 100,
        f"{value:,}\n({percentage:.1f}%)",
        ha="center",
        va="bottom",
        fontsize=11,
        fontweight="bold"
    )

ax.set_ylim(0, max(churn_counts.values) * 1.18)

plt.tight_layout()

plt.savefig(
    "output/churn_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()



# CHURN RATE BY SUBSCRIPTION


subscription_churn = (
    df.groupby("Subscription_Type")["Churn"]
    .mean()
    .mul(100)
    .sort_values(ascending=False)
)

fig, ax = plt.subplots(figsize=(9, 6))

bars = ax.bar(
    subscription_churn.index,
    subscription_churn.values,
    width=0.55
)

ax.set_title(
    "Churn Rate by Subscription Type",
    fontsize=18,
    fontweight="bold",
    pad=20
)

ax.set_ylabel("Churn Rate (%)", fontsize=11)

ax.grid(axis="y")
ax.grid(axis="x", visible=False)

for bar, value in zip(bars, subscription_churn.values):

    ax.text(
        bar.get_x() + bar.get_width() / 2,
        value + 0.15,
        f"{value:.2f}%",
        ha="center",
        va="bottom",
        fontsize=11,
        fontweight="bold"
    )

ax.set_ylim(
    subscription_churn.min() - 1,
    subscription_churn.max() + 1
)

plt.tight_layout()

plt.savefig(
    "output/churn_by_subscription.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()



# CHURN RATE BY TENURE
tenure_order = [
    "0-12 Months",
    "13-24 Months",
    "25-36 Months",
    "37-48 Months",
    "49-60 Months"
]

tenure_churn = (
    df.groupby("Tenure_Category", observed=False)["Churn"]
    .mean()
    .mul(100)
    .reindex(tenure_order)
)

fig, ax = plt.subplots(figsize=(10, 6))

bars = ax.bar(
    tenure_churn.index,
    tenure_churn.values,
    width=0.6
)

ax.set_title(
    "Churn Rate by Customer Tenure",
    fontsize=18,
    fontweight="bold",
    pad=20
)

ax.set_xlabel("Customer Tenure", fontsize=11)
ax.set_ylabel("Churn Rate (%)", fontsize=11)

ax.grid(axis="y")
ax.grid(axis="x", visible=False)

for bar, value in zip(bars, tenure_churn.values):

    ax.text(
        bar.get_x() + bar.get_width() / 2,
        value + 0.15,
        f"{value:.2f}%",
        ha="center",
        va="bottom",
        fontsize=10,
        fontweight="bold"
    )

plt.xticks(rotation=15)

ax.set_ylim(
    tenure_churn.min() - 1,
    tenure_churn.max() + 1
)

plt.tight_layout()

plt.savefig(
    "output/churn_by_tenure.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()



# CHURN RATE BY SATISFACTION
satisfaction_order = [
    "Low",
    "Medium",
    "Good",
    "Excellent"
]

satisfaction_churn = (
    df.groupby("Satisfaction_Level", observed=False)["Churn"]
    .mean()
    .mul(100)
    .reindex(satisfaction_order)
)

fig, ax = plt.subplots(figsize=(9, 6))

bars = ax.bar(
    satisfaction_churn.index,
    satisfaction_churn.values,
    width=0.6
)

ax.set_title(
    "Churn Rate by Satisfaction Level",
    fontsize=18,
    fontweight="bold",
    pad=20
)

ax.set_xlabel("Satisfaction Level", fontsize=11)
ax.set_ylabel("Churn Rate (%)", fontsize=11)

ax.grid(axis="y")
ax.grid(axis="x", visible=False)

for bar, value in zip(bars, satisfaction_churn.values):

    ax.text(
        bar.get_x() + bar.get_width() / 2,
        value + 0.15,
        f"{value:.2f}%",
        ha="center",
        va="bottom",
        fontsize=10,
        fontweight="bold"
    )

ax.set_ylim(
    satisfaction_churn.min() - 1,
    satisfaction_churn.max() + 1
)

plt.tight_layout()

plt.savefig(
    "output/churn_by_satisfaction.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()



# MONTHLY REVENUE AT RISK
revenue_risk = (
    df[df["Churn"] == 1]
    .groupby("Subscription_Type")["Monthly_Spending"]
    .sum()
    .sort_values(ascending=False)
)

fig, ax = plt.subplots(figsize=(9, 6))

bars = ax.bar(
    revenue_risk.index,
    revenue_risk.values,
    width=0.55
)

ax.set_title(
    "Monthly Revenue at Risk by Subscription",
    fontsize=18,
    fontweight="bold",
    pad=20
)

ax.set_ylabel("Monthly Revenue at Risk", fontsize=11)

ax.grid(axis="y")
ax.grid(axis="x", visible=False)

for bar, value in zip(bars, revenue_risk.values):

    ax.text(
        bar.get_x() + bar.get_width() / 2,
        value + 3000,
        f"{value:,.0f}",
        ha="center",
        va="bottom",
        fontsize=10,
        fontweight="bold"
    )

ax.set_ylim(0, max(revenue_risk.values) * 1.18)

plt.tight_layout()

plt.savefig(
    "output/revenue_at_risk_subscription.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()



# CHURN RATE BY LOCATION
location_churn = (
    df.groupby("Location")["Churn"]
    .mean()
    .mul(100)
    .sort_values(ascending=True)
)

fig, ax = plt.subplots(figsize=(10, 6))

bars = ax.barh(
    location_churn.index,
    location_churn.values,
    height=0.55
)

ax.set_title(
    "Churn Rate by Location",
    fontsize=18,
    fontweight="bold",
    pad=20
)

ax.set_xlabel("Churn Rate (%)", fontsize=11)

ax.grid(axis="x")
ax.grid(axis="y", visible=False)

for bar, value in zip(bars, location_churn.values):

    ax.text(
        value + 0.1,
        bar.get_y() + bar.get_height() / 2,
        f"{value:.2f}%",
        va="center",
        fontsize=10,
        fontweight="bold"
    )

ax.set_xlim(
    location_churn.min() - 1,
    location_churn.max() + 1
)

plt.tight_layout()

plt.savefig(
    "output/churn_by_location.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()



# COMPLETED
print("\n" + "=" * 50)
print("ALL VISUALIZATIONS GENERATED SUCCESSFULLY")
print("=" * 50)

print("\nGenerated files:")

for file in sorted(os.listdir("output")):
    print("✓", file)