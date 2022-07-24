-- distance calculation between two points by lat & lon
-- https://www.mrexcel.com/board/threads/calculating-distance-between-two-latitude-longitude-points.202255/
SELECT * FROM (SELECT station_id, address, station_name, (3959 * ACOS(COS(RADIANS(43.661896)) * COS(RADIANS(latitude))
* COS(RADIANS(longitude) - RADIANS(-79.396160)) + SIN(RADIANS(43.661896)) *
SIN(RADIANS(latitude))))
AS distance
FROM toronto_bike_stations ) a WHERE a.distance<15 ORDER BY a.distance ASC LIMIT 5;