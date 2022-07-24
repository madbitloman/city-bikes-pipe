import json
import requests
import pandas as pd
import logging
import os
from datetime import datetime

logging.basicConfig(level=logging.INFO)


def ts_folder_creation(df, product_type='bikes'):
    """Method to create a partitioned csv store.
    df: data frame to store
    product_type: """
    mydir = os.path.join(
        os.getcwd(), product_type,
        datetime.now().strftime('%Y-%m-%d_%H'))
    try:
        os.makedirs(mydir)
    except OSError as e:
        return logging.info("Folder already exists: {}".format(e))  # This was not a "directory exist" error..

    filename_path = mydir + '/' + '{}.csv'.format(product_type)
    df.to_csv(filename_path, index=False)
    logging.info("Data stored at --> {}".format(filename_path))


def df_get_json(url):
    """Method to call the API links
    url: given links"""
    try:
        r = requests.get(url=url)
        if not r.status_code == 200:
            return logging.info('Error: Could not get the data {}'.format(r.status_code))
        to_json = json.loads(r.text)
        return to_json
    except requests.exceptions.RequestException as e:
        return logging.info("Error: {}".format(e))


def get_info(url_info):
    """Simple function to get the stations info, normalize and convert it to Pandas
    dataframe"""
    info_json = df_get_json(url_info)
    df_info = pd.json_normalize(info_json['data'], "stations")
    return df_info


def get_status(url_status):
    """Simple function to get the stations status, normalize and convert it to Pandas
     dataframe"""
    status_json = df_get_json(url_status)
    df_status = pd.json_normalize(status_json['data'], "stations")
    df_status['last_updated'] = status_json['last_updated']
    return df_status


def main():

    status_url = 'https://tor.publicbikesystem.net/ube/gbfs/v1/en/station_status'
    info_url = 'https://tor.publicbikesystem.net/ube/gbfs/v1/en/station_information'

    logging.info('Starting the process')

    df_info = get_info(info_url)
    df_status = get_status(status_url)
    df_combined = pd.merge(df_info, df_status, on=['station_id', 'is_charging_station'])

    # usually, better to lower() strings before filtering
    df_combined = df_combined[df_combined.status == 'IN_SERVICE']
    # format timestamps
    df_combined['last_updated'] = df_combined.last_updated.apply(datetime.fromtimestamp)
    df_combined['last_reported'] = df_combined.last_reported.apply(datetime.fromtimestamp)

    # storing data to csv with ts folder path
    ts_folder_creation(df_combined)
    logging.info('Data extract finished!')


if __name__ == "__main__":
    main()
