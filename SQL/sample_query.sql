--SELECT * 
--FROM startups;

-- total companies = 70
--SELECT COUNT(*)
--FROM startups;

-- identify total valuation in table
--SELECT SUM(valuation)
--FROM startups;

-- identify maximum money raised (avail for startup - 11500000000)
--add during 'seed' stage (1,800,000)
--SELECT MAX(raised)
--FROM startups
--WHERE stage = 'Seed';

-- what year is the oldest company founded?
--SELECT MIN(founded), name
--FROM startups
--ORDER BY founded;

-- return average valuation
--SELECT ROUND(AVG(valuation), 2)
--FROM startups;

-- return average valuation by category, then round to 2 decimal
-- finally order by high to low on valuations avg
--SELECT category, ROUND(AVG(valuation), 2)
--FROM startups
--GROUP BY category
--ORDER BY 2 DESC;

-- filter result base on more than 3 companies in category
--SELECT category, count(*) AS counter
--FROM startups
--GROUP BY category
--HAVING counter > 3;

-- find average size startup by locations, then filter by size > 500
--SELECT location, ROUND(AVG(employees), 0) AS size
--FROM startups
--GROUP BY location
--HAVING size > 500;
