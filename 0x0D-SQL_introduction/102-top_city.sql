-- Shows top 3 hottest cities in July and August.
SELECT city, AVG(value) AS avg_temp FROM temperatures
WHERE month = 7 OR month = 8
GROUP BY city
ORDER BY avg_temp DESC;
LIMIT 3;
