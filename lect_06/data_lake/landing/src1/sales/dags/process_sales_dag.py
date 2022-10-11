from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'ArtemChumachenko',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}
with DAG(
    'first_sales_api_dag',
    default_args=default_args,
    description='Dag for triggering api and save files in json and avro',
    schedule_interval='0 1 * * *',
    start_date=datetime(2022, 8, 9, 0, 0, 1),
    end_date=datetime(2022, 8, 11, 0, 0, 1),
    catchup=False
) as dag:
    t1 = BashOperator(
        task_id='extract_data_from_api',
        bash_command='python /Users/macbook/Documents/GitHub/de2022_last/lect_06/data_lake/landing/src1/sales/dags/api_to_json.py --date {{ ds }}'
    )

    t2 = BashOperator(
        task_id='convert_to_avro',
        bash_command='python /Users/macbook/Documents/GitHub/de2022_last/lect_06/data_lake/landing/src1/sales/dags/json_to_avro.py --date {{ ds }}'
    )

    t2.set_upstream(t1)
