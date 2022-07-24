

class OcTestUtils:

    def __engine_creation__(db_type=None):
        'Simple function to create SQL engine based on the credentials type'
        with open("config/db_config.yml", 'r') as ymlfile:
            cfg = yaml.load(ymlfile)

        db_connection_str = 'postgresql://{usr}:{pwd}@{host}/{db}'.format(usr=cfg[db_type]['usr'],
                                                                             pwd=cfg[db_type]['pwd'],
                                                                             host=cfg[db_type]['host'],
                                                                             db=cfg[db_type]['db'])

        engine = create_engine(db_connection_str)

        return engine

    @staticmethod
    def columns_to_keep():

        set_of_columns = {"station_id", "station_name", "physical_configuration", "latitude", "longitude", "altitude",
                          "address", "capacity", "rental_methods", "groups", "obcn", "nearby_distance",
                          "num_bikes_available", "mechanical_bikes_available", "electric_bikes_available",
                          "num_bikes_disabled", "num_docks_available", "num_docks_disabled", "is_installed",
                          "is_renting", "is_returning",  "last_reported", "is_charging_station", "status"}

        return set_of_columns
