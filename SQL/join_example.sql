-- Perform left join to require inclusion of all table objects in first(left) table

SELECT *
FROM newspaper 
LEFT JOIN online
	ON newspaper.id = online.id;
  
SELECT *
FROM newspaper 
LEFT JOIN online
	ON newspaper.id = online.id
WHERE online.id IS NULL;


-- CROSS JOIN

SELECT COUNT(*)
FROM newspaper
WHERE start_month < 3 AND end_month > 3;

SELECT *
FROM newspaper
CROSS JOIN months;

SELECT *
FROM newspaper
CROSS JOIN months
WHERE month > start_month AND month < end_month;

SELECT month, COUNT(*) AS subscribers
FROM newspaper
CROSS JOIN months
WHERE month > start_month AND month < end_month
GROUP BY month;

-- UNION (require matching columns and datatypes

SELECT *
FROM newspaper
UNION
SELECT *
FROM online;

-- WITH clause

WITH previous_query AS (
	SELECT customer_id, COUNT(subscription_id) as subscriptions
	FROM orders
	GROUP BY customer_id
)
SELECT customers.customer_name, previous_query.subscriptions
FROM previous_query 
JOIN customers 
	ON previous_query.customer_id = customers.customer_id;
