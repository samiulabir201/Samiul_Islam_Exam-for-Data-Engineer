from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

# Airflow DAG definition
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 3, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'chef_jobs_extraction',
    default_args=default_args,
    description='DAG to extract chef jobs data and upload to MongoDB',
    schedule_interval='0 0 1 * *',  # Run at 12 AM on the first day of each month
)

# PythonOperator to execute the data extraction and upload function
extract_and_upload_task = PythonOperator(
    task_id='extract_and_upload_task',
    python_callable =lambda: exec(open('E:\Python_DAG\scripts\Chefs_Job_Scrapper.py').read()),
    dag=dag,
)

# Set task dependencies
extract_and_upload_task
