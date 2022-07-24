import pandas as pd
import yaml
import logging
import os
from datetime import datetime
from sqlalchemy import create_engine


logging.basicConfig(level=logging.INFO)


def __engine_creation__(db_type=None):
    """Function to create Postgres engine based on the credentials type"""
    with open("config/db_config.yml", 'r') as ymlfile:
        cfg = yaml.load(ymlfile)

    db_connection_str = 'postgresql://{usr}:{pwd}@{host}/{db}'.format(usr=cfg[db_type]['usr'],
                                                                      pwd=cfg[db_type]['pwd'],
                                                                      host=cfg[db_type]['host'],
                                                                      db=cfg[db_type]['db'])

    engine = create_engine(db_connection_str)
    return engine


def columns_to_keep():
    """Rather for aesthetics we keep the set of immutable variables names that needed to be exported to the DB"""
    set_of_columns = {"station_id", "station_name", "physical_configuration", "latitude", "longitude", "altitude",
                      "address", "capacity", "rental_methods", "groups", "obcn", "nearby_distance",
                      "num_bikes_available", "mechanical_bikes_available", "electric_bikes_available",
                      "num_bikes_disabled", "num_docks_available", "num_docks_disabled", "is_installed",
                      "is_renting", "is_returning", "last_reported", "is_charging_station", "status"}

    return set_of_columns


def bikes_csv_reader(product_type='bikes'):
    path = os.path.join(
        os.getcwd(), product_type,
        datetime.now().strftime('%Y-%m-%d_%H'))

    if os.path.isdir(path) and os.path.exists(path):
        if len(os.listdir(path)) == 0:
            logging.info('Hmmm! Looks like data is missing! Please check pipeline.')
        else:
            path_to_file = path + '/' + 'bikes.csv'

    df_bikes = pd.read_csv(path_to_file)

    df_bikes = df_bikes.rename(columns={"name": "station_name", "lat": "latitude", "lon": "longitude",
                                        "num_bikes_available_types.mechanical": "mechanical_bikes_available",
                                        "num_bikes_available_types.ebike": "electric_bikes_available"},
                               errors="raise")

    df_bikes = df_bikes[columns_to_keep()]

    return df_bikes


def main():

    df_bikes_for_export = bikes_csv_reader()

    df_bikes_for_export.to_sql(name="toronto_bike_stations", con=__engine_creation__('pg_bikes_data'),
                               index=False, if_exists='append')

    logging.info('Success! All data imported!')


if __name__ == "__main__":
    main()
