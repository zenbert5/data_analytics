-- basic arithmetics
-- count rows / 2

SELECT COUNT(*) / 2
FROM referrals;

-- count number of referrers in referrals table by total users for a ratio

SELECT 1.0 * COUNT(referrals.referrer_id) / COUNT(users.id)
FROM users
LEFT JOIN referrals
	ON users.id = referrals.referrer_id;

-- identify distinct users by total users count

SELECT COUNT(*)
FROM referrals;

SELECT 1.0 * COUNT(scoopons.user_id) / COUNT(DISTINCT scoopons.user_id)
FROM scoopons;


-- calculate minimal percentage increase to achieve the goal of +$100/week
-- 417 referrals, users buy 3.2 scoopons, each scoopoon = $1, referrer saves $.50
-- what's the minimum increase in referrals to reach goal?
import numpy as np

current_revenue = 417 * 3.20

revenue_per_referred = 3.20 - 0.50

goal_referrals = (current_revenue + 100.0) / revenue_per_referred
print goal_referrals

min_diff = np.rint(100.0 * (goal_referrals - 417) / 417.0)
print min_diff
