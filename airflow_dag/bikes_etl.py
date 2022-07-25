import os
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime


cwd = os.environ['AIRFLOW_HOME'] + '/dags/scripts'
os.chdir(cwd)
START_DATE = datetime(2022, 7, 23)


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': START_DATE,
    'on_failure_callback': None,
}

dag = DAG('bikes_etl_dag', default_args=default_args, catchup=False, schedule_interval='0 * * * *')


data_import_cmd = "python3 data_import.py"
data_import = BashOperator(
    task_id='data_import',
    bash_command=data_import_cmd,
    dag=dag
)

data_export_cmd = "python3 data_export.py"
data_export = BashOperator(
    task_id='data_export',
    bash_command=data_export_cmd,
    dag=dag
)

# email or slack? ez pz
report_cmd = "python3 report.py"
hourly_report = BashOperator(
    task_id='hourl_report_task',
    bash_command=report_cmd,
    dag=dag
)

cleanup = BashOperator(
    task_id='report_files_cleanup',
    bash_command="rm -r /home/ubuntu/airflow/dags/scripts/*_report.*",
    dag=dag
)

data_import >> data_export >> hourly_report >> cleanup
