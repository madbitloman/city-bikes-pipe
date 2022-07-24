import pandas as pd
import subprocess
from data_export import __engine_creation__


def get_query(q_type):
    """Method to read all the needed *.sql files from queries folder.
    q_type: type of the query from the test to run"""

    local_path = 'queries/{}.sql'.format(q_type)
    with open(local_path, 'r') as sql_f:
        query_string = sql_f.read()

    return query_string


def pandas_table_setting():
    """Simple method to set Pandas CSS for tables"""
    th_props = [('font-size', '26px'), ('text-align', 'center'), ('font-weight', 'bold'), ('color', '#6d6d6d'),
                ('background-color', '#f7f7f9')]

    td_props = [('font-size', '26px'), ('text-align', 'center')]

    styles = [dict(selector="th", props=th_props), dict(selector="td", props=td_props)]
    return styles


def main():
    styles = pandas_table_setting()

    bikes = pd.read_sql(get_query('available_bikes'), con=__engine_creation__('pg_bikes_data'))

    available_bikes_toronto = pd.read_sql(get_query('available_bikes_toronto'),
                                          con=__engine_creation__('pg_bikes_data'))

    avg_bikes_available = pd.read_sql(get_query('avg_bikes_available'), con=__engine_creation__('pg_bikes_data'))

    largest_stations = pd.read_sql(get_query('top_3_capacity_stations'), con=__engine_creation__('pg_bikes_data'))
    largest_stations_html = largest_stations.style.set_table_styles(styles).background_gradient().hide_index().render()

    small_stations = pd.read_sql(get_query('bottom_3_capacity_stations'), con=__engine_creation__('pg_bikes_data'))
    smallest_stations_html = small_stations.style.set_table_styles(styles).background_gradient().hide_index().render()

    imaginary_loc = pd.read_sql(get_query('imaginary_location'), con=__engine_creation__('pg_bikes_data'))
    imaginary_loc_html = imaginary_loc.style.set_table_styles(styles).background_gradient().hide_index().render()

    with open('config/template.html', 'r') as html:
        html_as_string = html.read()
    with open('report.html', 'w') as f:
        f.write(html_as_string.format(available_bikes=format(int(bikes.bikes_available), ".0f"),
                                      bikes_available_t=format(int(available_bikes_toronto.bikes_available_t), ".0f"),
                                      avg_bikes=format(int(avg_bikes_available.avg_bikes_available), ".0f"),
                                      largest_stations=largest_stations_html, small_stations=smallest_stations_html,
                                      imaginary_loc=imaginary_loc_html))

    # Had to do this mambo jambo to generate proper PDF from HTML knitted report
    report_name = '{type}_report.pdf'.format(type='hourly_bike_report')
    subprocess.call(
            # uncomment line below if compiled on Linux -->
            # 'xvfb-run --server-args="-screen 0, 1280x768x24" '
            'wkhtmltopdf --zoom 0.9 report.html {report_name}'.format(report_name=report_name), shell=True)


if __name__ == "__main__":
    main()
