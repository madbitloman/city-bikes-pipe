DROP TABLE IF EXISTS toronto_bike_stations;

CREATE TABLE toronto_bike_stations (
last_updated TIMESTAMPTZ NOT NULL DEFAULT NOW(),
station_id INT PRIMARY KEY,
station_name VARCHAR ( 50 ) UNIQUE NOT NULL,
physical_configuration VARCHAR ( 50 ),
latitude FLOAT NOT NULL,
longitude FLOAT NOT NULL,
altitude FLOAT DEFAULT 0.0,
address VARCHAR ( 240 ),
capacity INT,
rental_methods VARCHAR ( 50 ),
groups VARCHAR ( 50 ),
obcn VARCHAR ( 50 ),
nearby_distance FLOAT NOT NULL,
num_bikes_available INT,
mechanical_bikes_available INT,
electric_bikes_available INT,
num_bikes_disabled INT,
num_docks_available INT,
num_dosck_disabled INT,
is_installed BYTEA,
is_renting BYTEA,
is_returning BYTEA,
last_reported TIMESTAMPTZ NOT NULL DEFAULT NOW(),
is_charging_station BYTEA,
status VARCHAR ( 50 )
);