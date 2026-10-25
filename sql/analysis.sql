SELECT airport_code, year, SUM(total_passengers) AS passengers FROM fact_monthly_traffic GROUP BY airport_code, year;
