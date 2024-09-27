from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

# Define the default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 9, 28),  # Set the start date
    'retries': 1,
}

# Define the DAG
with DAG('bash_operator_dag',
         default_args=default_args,
         schedule_interval='@once',  # Runs once
         catchup=False) as dag:

    # Task to print "Hello, World!" using BashOperator
    hello_bash = BashOperator(
        task_id='hello_bash',
        bash_command='echo "Hello, World from BashOperator!"'
    )
