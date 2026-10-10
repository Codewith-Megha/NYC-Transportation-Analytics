"""
SQL queries for Transportation Analytics Dashboard
"""

# =====================================================
# KPI QUERIES
# =====================================================

TOTAL_TRIPS = """
SELECT COUNT(*) AS total_trips
FROM yellow_trips;
"""

TOTAL_REVENUE = """
SELECT ROUND(SUM(total_amount)::numeric,2) AS total_revenue
FROM yellow_trips;
"""

AVERAGE_TRIP_DISTANCE = """
SELECT ROUND(AVG(trip_distance)::numeric,2) AS avg_trip_distance
FROM yellow_trips;
"""

AVERAGE_TRIP_DURATION = """
SELECT ROUND(AVG(trip_duration_minutes)::numeric,2) AS avg_trip_duration
FROM yellow_trips;
"""

AVERAGE_FARE_OVERALL = """
SELECT ROUND(AVG(fare_amount)::numeric,2) AS avg_fare
FROM yellow_trips;
"""

# =====================================================
# TRIP ANALYSIS
# =====================================================

MONTHLY_TRIPS = """
SELECT
    pickup_month,
    COUNT(*) AS total_trips
FROM yellow_trips
GROUP BY pickup_month
ORDER BY pickup_month;
"""

WEEKDAY_TRIPS = """
SELECT
    pickup_weekday,
    COUNT(*) AS total_trips
FROM yellow_trips
GROUP BY pickup_weekday
ORDER BY total_trips DESC;
"""

HOURLY_TRIPS = """
SELECT
    pickup_hour,
    COUNT(*) AS total_trips
FROM yellow_trips
GROUP BY pickup_hour
ORDER BY pickup_hour;
"""

WEEKEND_ANALYSIS = """
SELECT
CASE
WHEN is_weekend THEN 'Weekend'
ELSE 'Weekday'
END AS day_type,
COUNT(*) AS total_trips
FROM yellow_trips
GROUP BY day_type;
"""

RUSH_HOUR = """
SELECT
CASE
WHEN rush_hour THEN 'Rush Hour'
ELSE 'Non Rush Hour'
END AS period,
COUNT(*) AS total_trips
FROM yellow_trips
GROUP BY period;
"""

PASSENGER_COUNT_DISTRIBUTION = """
SELECT
    passenger_count,
    COUNT(*) AS total_trips
FROM yellow_trips
GROUP BY passenger_count
ORDER BY passenger_count;
"""

TRIP_CATEGORY = """
SELECT
    CASE
        WHEN trip_category IS NOT NULL THEN trip_category
        WHEN trip_distance = 0 THEN 'Zero distance'
        ELSE 'Unknown'
    END AS trip_category,
    COUNT(*) AS total_trips
FROM yellow_trips
GROUP BY 1
ORDER BY total_trips DESC;
"""

# =====================================================
# REVENUE ANALYSIS
# =====================================================

MONTHLY_REVENUE = """
SELECT
    pickup_month,
    ROUND(SUM(total_amount)::numeric,2) AS revenue
FROM yellow_trips
GROUP BY pickup_month
ORDER BY pickup_month;
"""

REVENUE_BY_HOUR = """
SELECT
    pickup_hour,
    ROUND(SUM(total_amount)::numeric,2) AS revenue
FROM yellow_trips
GROUP BY pickup_hour
ORDER BY pickup_hour;
"""

AVERAGE_FARE = """
SELECT
    pickup_month,
    ROUND(AVG(fare_amount)::numeric,2) AS average_fare
FROM yellow_trips
GROUP BY pickup_month
ORDER BY pickup_month;
"""

# =====================================================
# SPEED & DISTANCE
# =====================================================

AVERAGE_DISTANCE = """
SELECT
    pickup_month,
    ROUND(AVG(trip_distance)::numeric,2) AS average_distance
FROM yellow_trips
GROUP BY pickup_month
ORDER BY pickup_month;
"""

AVERAGE_DURATION = """
SELECT
    pickup_month,
    ROUND(AVG(trip_duration_minutes)::numeric,2) AS average_duration
FROM yellow_trips
GROUP BY pickup_month
ORDER BY pickup_month;
"""

HOURLY_AVERAGE_SPEED = """
SELECT
    pickup_hour,
    ROUND(AVG(average_speed_mph)::numeric,2) AS average_speed
FROM yellow_trips
GROUP BY pickup_hour
ORDER BY pickup_hour;
"""

MONTHLY_AVERAGE_SPEED = """
SELECT
    pickup_month,
    ROUND(AVG(average_speed_mph)::numeric,2) AS average_speed
FROM yellow_trips
GROUP BY pickup_month
ORDER BY pickup_month;
"""

# =====================================================
# LOCATION ANALYSIS
# =====================================================

TOP_PICKUPS = """
SELECT
    pulocationid,
    COUNT(*) AS trips
FROM yellow_trips
GROUP BY pulocationid
ORDER BY trips DESC
LIMIT 10;
"""

TOP_DROPOFFS = """
SELECT
    dolocationid,
    COUNT(*) AS trips
FROM yellow_trips
GROUP BY dolocationid
ORDER BY trips DESC
LIMIT 10;
"""

TOP_REVENUE_LOCATIONS = """
SELECT
    pulocationid,
    ROUND(SUM(total_amount)::numeric,2) AS revenue
FROM yellow_trips
GROUP BY pulocationid
ORDER BY revenue DESC
LIMIT 10;
"""


# =====================================================
# GREEN TAXI ANALYSIS
# =====================================================

GREEN_MONTHLY_TRIPS = """
SELECT
    pickup_month,
    COUNT(*) AS total_trips
FROM green_trips
GROUP BY pickup_month
ORDER BY pickup_month;
"""

# =====================================================
# FHV ANALYSIS
# =====================================================

FHV_MONTHLY_TRIPS = """
SELECT
    pickup_month,
    COUNT(*) AS total_trips
FROM fhv_trips
GROUP BY pickup_month
ORDER BY pickup_month;
"""

# =====================================================
# OTHER ANALYSIS
# =====================================================

PAYMENT_TYPES = """
SELECT
CASE
    WHEN payment_type = 1 THEN 'Credit Card'
    WHEN payment_type = 2 THEN 'Cash'
    WHEN payment_type = 3 THEN 'No Charge'
    WHEN payment_type = 4 THEN 'Dispute'
    WHEN payment_type = 5 THEN 'Unknown'
    WHEN payment_type = 6 THEN 'Voided Trip'
    ELSE 'Missing'
END AS payment_method,
COUNT(*) AS total_trips
FROM yellow_trips
GROUP BY payment_method
ORDER BY total_trips DESC;
"""

DATASET_COMPARISON = """
SELECT dataset, total_trips
FROM (
    SELECT 1 AS sort_order, 'Yellow' AS dataset, COUNT(*) AS total_trips
    FROM yellow_trips

    UNION ALL

    SELECT 2, 'Green', COUNT(*)
    FROM green_trips

    UNION ALL

    SELECT 3, 'FHV', COUNT(*)
    FROM fhv_trips
) t
ORDER BY sort_order;
"""