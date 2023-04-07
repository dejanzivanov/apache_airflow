from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor

default_args = {
    'owner':'dejan',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}


with DAG(
    dag_id = 'dag_minion_s3_v03',
    start_date = datetime(2023, 4, 1),
    schedule_interval='@daily',
    default_args=default_args
) as dag:
    pass

    task1 = S3KeySensor(
        task_id = 'sensor_minio_s3',
        bucket_name = 'airflow',
        bucket_key = 'data.csv',
        aws_conn_id = 'minio_s3_conn'
    )
    