from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 3, 11),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'DAG_1',
    default_args=default_args,
    description='DAG to execute first and second scrappers',
    schedule_interval='0 0 * * 0',  # Weekly on Sunday at 12 AM
)

def first_scraper():
    exec(open('E:\Python_DAG\scripts\First_scrapper.py').read())

def second_scraper():
    exec(open('E:\Python_DAG\scripts\Second_scrapper.py').read())

# Define tasks
task_first_scraper = PythonOperator(
    task_id='first_scraper',
    python_callable=first_scraper,
    dag=dag,
)

task_second_scraper = PythonOperator(
    task_id='second_scraper',
    python_callable=second_scraper,
    dag=dag,
)

# Set task dependencies
task_first_scraper >> task_second_scraper
