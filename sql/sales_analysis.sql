-- Store/day sales analysis
SELECT
    store_id,
    sale_date,
    SUM(total_amount) AS total_sales,
    SUM(quantity) AS units_sold,
    COUNT(DISTINCT transaction_id) AS transaction_count
FROM silver_sales
GROUP BY store_id, sale_date
ORDER BY sale_date, total_sales DESC;
