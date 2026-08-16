-- Customer sales analysis
SELECT
    customer_code,
    SUM(total_amount) AS total_sales,
    COUNT(DISTINCT transaction_id) AS transaction_count
FROM silver_sales
GROUP BY customer_code
ORDER BY total_sales DESC;
