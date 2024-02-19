SELECT *
FROM yellow_taxi_trips
LIMIT 100;

SELECT * FROM zones;

SELECT *
FROM	yellow_taxi_trips t,
		zones zpu,
		zones zdo
WHERE t."PULocationID" = zpu."LocationID" AND
	  t."DOLocationID" = zdo."LocationID"
LIMIT 100;

-- Select pickup datetime, dropoff datetime, total amount, pickup location and drop location

SELECT tpep_pickup_datetime,
	   tpep_dropoff_datetime,
	   total_amount,
	   CONCAT(zpu."Borough", '/', zpu."Zone") AS "pickup_loc",
	   CONCAT(zdo."Borough", '/', zdo."Zone") AS "dropoff_loc"
FROM	yellow_taxi_trips t,
		zones zpu,
		zones zdo
WHERE t."PULocationID" = zpu."LocationID" AND
	  t."DOLocationID" = zdo."LocationID"
LIMIT 100;

-- Using JOIN

SELECT 
	tpep_pickup_datetime,
	tpep_dropoff_datetime,
   	total_amount,
   	CONCAT(zpu."Borough", '/', zpu."Zone") AS "pickup_loc",
   	CONCAT(zdo."Borough", '/', zdo."Zone") AS "dropoff_loc"
FROM   
	yellow_taxi_trips t 
	JOIN zones zpu
		ON t."PULocationID" = zpu."LocationID" 
	JOIN zones zdo
		ON t."DOLocationID" = zdo."LocationID"
LIMIT 100;

-- Other JOINs
-- LEFT JOIN
-- RIGHT JOIN
-- OUTER JOIN

-- Calculate number of trips each day by drop location

SELECT 
   	CAST(tpep_pickup_datetime AS DATE) AS pickup_date,
	"DOLocationID",
	COUNT(1) AS trip_count
FROM   
	yellow_taxi_trips
GROUP BY
	1, 2
ORDER BY
	1, 2;