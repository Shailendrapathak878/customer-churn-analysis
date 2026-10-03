SELECT current_database();

CREATE TABLE public.customer_churn (
    customer_id VARCHAR(50) PRIMARY KEY,
    age INTEGER,
    gender VARCHAR(20),
    location VARCHAR(50),
    subscription_type VARCHAR(30),
    account_age_months INTEGER,
    monthly_spending NUMERIC(10,2),
    total_usage_hours INTEGER,
    support_calls INTEGER,
    late_payments INTEGER,
    streaming_usage INTEGER,
    discount_used INTEGER,
    satisfaction_score INTEGER,
    last_interaction_type VARCHAR(30),
    complaint_tickets INTEGER,
    promo_opted_in INTEGER,
    churn INTEGER,
    tenure_category VARCHAR(20),
    spending_category VARCHAR(20),
    usage_intensity NUMERIC(10,2),
    support_intensity INTEGER,
    payment_risk VARCHAR(20),
    satisfaction_level VARCHAR(20),
    customer_value NUMERIC(12,2)
);
SELECT table_schema, table_name
FROM information_schema.tables
WHERE table_schema = 'public';

SELECT COUNT(*) 
FROM customer_churn;

SELECT *
FROM customer_churn
LIMIT 10;


SELECT 
    churn,
    COUNT(*) AS customer_count
FROM customer_churn
GROUP BY churn
ORDER BY churn;

 --Overall Business KPIs

SELECT
    COUNT(*) AS total_customers,
    SUM(churn) AS churned_customers,
    COUNT(*) - SUM(churn) AS active_customers,
    ROUND(100.0 * SUM(churn) / COUNT(*), 2) AS churn_rate,
    ROUND(AVG(monthly_spending), 2) AS avg_monthly_spending,
    ROUND(AVG(account_age_months), 2) AS avg_account_age
FROM customer_churn;

--Churn by Subscription Type
SELECT
    subscription_type,
    COUNT(*) AS total_customers,
    SUM(churn) AS churned_customers,
    ROUND(100.0 * SUM(churn) / COUNT(*), 2) AS churn_rate
FROM customer_churn
GROUP BY subscription_type
ORDER BY churn_rate DESC;

--Churn by Location
SELECT
    location,
    COUNT(*) AS total_customers,
    SUM(churn) AS churned_customers,
    ROUND(100.0 * SUM(churn) / COUNT(*), 2) AS churn_rate
FROM customer_churn
GROUP BY location
ORDER BY churn_rate DESC;


--Churn by Gender
SELECT
    gender,
    COUNT(*) AS total_customers,
    SUM(churn) AS churned_customers,
    ROUND(100.0 * SUM(churn) / COUNT(*), 2) AS churn_rate
FROM customer_churn
GROUP BY gender
ORDER BY churn_rate DESC;


--Churn by Last Interaction
SELECT
    last_interaction_type,
    COUNT(*) AS total_customers,
    SUM(churn) AS churned_customers,
    ROUND(100.0 * SUM(churn) / COUNT(*), 2) AS churn_rate
FROM customer_churn
GROUP BY last_interaction_type
ORDER BY churn_rate DESC;

--Churn by Tenure Category
SELECT
    tenure_category,
    COUNT(*) AS customers,
    SUM(churn) AS churned_customers,
    ROUND(100.0 * SUM(churn) / COUNT(*), 2) AS churn_rate
FROM customer_churn
GROUP BY tenure_category
ORDER BY churn_rate DESC;

--Churn by Spending Category
SELECT
    spending_category,
    COUNT(*) AS customers,
    SUM(churn) AS churned_customers,
    ROUND(100.0 * SUM(churn) / COUNT(*), 2) AS churn_rate
FROM customer_churn
GROUP BY spending_category
ORDER BY churn_rate DESC;

--Churn by Payment Risk
SELECT
    payment_risk,
    COUNT(*) AS customers,
    SUM(churn) AS churned_customers,
    ROUND(100.0 * SUM(churn) / COUNT(*), 2) AS churn_rate
FROM customer_churn
GROUP BY payment_risk
ORDER BY churn_rate DESC;


--Churn by Satisfaction Level
SELECT
    satisfaction_level,
    COUNT(*) AS customers,
    SUM(churn) AS churned_customers,
    ROUND(100.0 * SUM(churn) / COUNT(*), 2) AS churn_rate
FROM customer_churn
GROUP BY satisfaction_level
ORDER BY churn_rate DESC;

--Churn by Support Intensity
SELECT
    support_intensity,
    COUNT(*) AS customers,
    SUM(churn) AS churned_customers,
    ROUND(100.0 * SUM(churn) / COUNT(*), 2) AS churn_rate
FROM customer_churn
GROUP BY support_intensity
ORDER BY support_intensity;

--Churn by Complaint Tickets
SELECT
    complaint_tickets,
    COUNT(*) AS customers,
    SUM(churn) AS churned_customers,
    ROUND(100.0 * SUM(churn) / COUNT(*), 2) AS churn_rate
FROM customer_churn
GROUP BY complaint_tickets
ORDER BY complaint_tickets;

--Churn by Promo Opt-In
SELECT
    promo_opted_in,
    COUNT(*) AS customers,
    SUM(churn) AS churned_customers,
    ROUND(100.0 * SUM(churn) / COUNT(*), 2) AS churn_rate
FROM customer_churn
GROUP BY promo_opted_in
ORDER BY churn_rate DESC;


--Customer Metrics: Churned vs Active
SELECT
    churn,
    COUNT(*) AS customers,
    ROUND(AVG(monthly_spending), 2) AS avg_spending,
    ROUND(AVG(account_age_months), 2) AS avg_tenure,
    ROUND(AVG(support_calls), 2) AS avg_support_calls,
    ROUND(AVG(satisfaction_score), 2) AS avg_satisfaction,
    ROUND(AVG(customer_value), 2) AS avg_customer_value
FROM customer_churn
GROUP BY churn
ORDER BY churn;

--Revenue at Risk by Subscription
SELECT
    subscription_type,
    COUNT(*) FILTER (WHERE churn = 1) AS churned_customers,
    ROUND(SUM(monthly_spending) FILTER (WHERE churn = 1), 2)
        AS monthly_revenue_at_risk
FROM customer_churn
GROUP BY subscription_type
ORDER BY monthly_revenue_at_risk DESC;

--Revenue at Risk by Location
SELECT
    location,
    COUNT(*) FILTER (WHERE churn = 1) AS churned_customers,
    ROUND(SUM(monthly_spending) FILTER (WHERE churn = 1), 2)
        AS monthly_revenue_at_risk
FROM customer_churn
GROUP BY location
ORDER BY monthly_revenue_at_risk DESC;

--Revenue at Risk by Tenure
SELECT
    tenure_category,
    COUNT(*) FILTER (WHERE churn = 1) AS churned_customers,
    ROUND(SUM(monthly_spending) FILTER (WHERE churn = 1), 2)
        AS monthly_revenue_at_risk
FROM customer_churn
GROUP BY tenure_category
ORDER BY monthly_revenue_at_risk DESC;

--High-Value Churned Customers
SELECT
    customer_id,
    location,
    subscription_type,
    account_age_months,
    monthly_spending,
    customer_value,
    satisfaction_score
FROM customer_churn
WHERE churn = 1
ORDER BY customer_value DESC
LIMIT 20;

--Churned Customers with High Support Activity
SELECT
    customer_id,
    support_calls,
    complaint_tickets,
    support_intensity,
    satisfaction_score,
    monthly_spending
FROM customer_churn
WHERE churn = 1
  AND support_intensity >= 8
ORDER BY support_intensity DESC, monthly_spending DESC;


--Churned Customers with Low Satisfaction
SELECT
    customer_id,
    satisfaction_score,
    satisfaction_level,
    subscription_type,
    monthly_spending,
    support_calls
FROM customer_churn
WHERE churn = 1
  AND satisfaction_score <= 3
ORDER BY satisfaction_score, monthly_spending DESC;

--Location + Satisfaction Analysis
SELECT
    location,
    satisfaction_level,
    COUNT(*) AS customers,
    SUM(churn) AS churned_customers,
    ROUND(100.0 * SUM(churn) / COUNT(*), 2) AS churn_rate
FROM customer_churn
GROUP BY location, satisfaction_level
HAVING COUNT(*) >= 50
ORDER BY churn_rate DESC;

--Rank Locations by Churn Rate
WITH location_churn AS (
    SELECT
        location,
        COUNT(*) AS customers,
        SUM(churn) AS churned_customers,
        100.0 * SUM(churn) / COUNT(*) AS churn_rate
    FROM customer_churn
    GROUP BY location
)

SELECT
    location,
    customers,
    churned_customers,
    ROUND(churn_rate, 2) AS churn_rate,
    RANK() OVER (ORDER BY churn_rate DESC) AS churn_rank
FROM location_churn
ORDER BY churn_rank;

--Which Subscription Generates Most Revenue at Risk?
WITH revenue_risk AS (
    SELECT
        subscription_type,
        SUM(monthly_spending) FILTER (WHERE churn = 1)
            AS revenue_at_risk
    FROM customer_churn
    GROUP BY subscription_type
)

SELECT
    subscription_type,
    ROUND(revenue_at_risk, 2) AS revenue_at_risk,
    ROUND(
        100.0 * revenue_at_risk /
        SUM(revenue_at_risk) OVER (),
        2
    ) AS percentage_of_total_risk
FROM revenue_risk
ORDER BY revenue_at_risk DESC;

--Customer Risk Segmentation
SELECT
    customer_id,
    subscription_type,
    monthly_spending,
    satisfaction_score,
    support_intensity,
    churn,
    CASE
        WHEN churn = 1 AND customer_value >= 5000
            THEN 'High Value Churned'
        WHEN churn = 1 AND satisfaction_score <= 3
            THEN 'Dissatisfied Churned'
        WHEN churn = 1 AND support_intensity >= 8
            THEN 'High Support Churned'
        WHEN churn = 1
            THEN 'Other Churned'
        ELSE 'Active'
    END AS customer_segment
FROM customer_churn;




