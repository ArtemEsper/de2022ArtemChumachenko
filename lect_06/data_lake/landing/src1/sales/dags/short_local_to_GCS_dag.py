from airflow import DAG
from datetime import datetime
from airflow.providers.google.cloud.transfers.local_to_gcs import LocalFilesystemToGCSOperator

dag = DAG(
    dag_id="example_dag_2",
    start_date=datetime(2022, 9, 16),
    schedule_interval="0 5 * * *",
    catchup=True,
)

gcp_operator = LocalFilesystemToGCSOperator(
    task_id='gcp_task',
    src='/Users/macbook/Documents/GitHub/de2022_last/lect_06/data_lake/landing/src1/sales',
    dst='gs://de2022_datalake_chumachenko',
    bucket='de2022_datalake_chumachenko',
    google_cloud_storage_conn_id='de2022-artem-chumachenko',
    mime_type='Folder',
    dag=dag
)
