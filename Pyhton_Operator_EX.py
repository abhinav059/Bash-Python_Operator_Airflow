from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Define a Python function for the PythonOperator
def print_hello():
    print("Hello, World from PythonOperator!")

# Define the default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 9, 28),  # Set the start date
    'retries': 1,
}

# Define the DAG
with DAG('python_operator_dag',
         default_args=default_args,
         schedule_interval='@once',  # Runs once
         catchup=False) as dag:

    # Task to print "Hello, World!" using PythonOperator
    hello_python = PythonOperator(
        task_id='hello_python',
        python_callable=print_hello
    )
