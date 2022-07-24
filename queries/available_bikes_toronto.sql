-- I use coordinates from top right and bottom left to separate Toronto from GTA (from Google Maps)
SELECT SUM(num_bikes_available) AS bikes_available_t FROM toronto_bike_stations
WHERE (latitude<=43.85514008064188 AND latitude>=43.581028109498284)
AND (longitude<=-79.17064808611549 AND longitude>=-79.54368114084102);