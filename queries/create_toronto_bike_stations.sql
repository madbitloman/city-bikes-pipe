DROP TABLE IF EXISTS toronto_bike_stations;

CREATE TABLE toronto_bike_stations (
last_updated TIMESTAMP NOT NULL DEFAULT NOW(),
station_id INT PRIMARY KEY,
station_name VARCHAR (50) UNIQUE NOT NULL,
physical_configuration VARCHAR (50),
latitude FLOAT NOT NULL,
longitude FLOAT NOT NULL,
altitude FLOAT DEFAULT 0.0,
address VARCHAR(255),
capacity INT,
rental_methods VARCHAR(255),
groups VARCHAR(255),
obcn VARCHAR (50),
nearby_distance FLOAT NOT NULL,
num_bikes_available INT,
mechanical_bikes_available INT,
electric_bikes_available INT,
num_bikes_disabled INT,
num_docks_available INT,
num_docks_disabled INT,
is_installed INT,
is_renting INT,
is_returning INT,
last_reported TIMESTAMP NOT NULL DEFAULT '2001-01-01 00:00:00',
is_charging_station BOOLEAN,
status VARCHAR (50)
);