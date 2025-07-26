from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'start_date': datetime(2025, 7, 26),
}

with DAG(
    dag_id='second_dag',
    default_args=default_args,
    schedule_interval=None,
    catchup=False
) as dag:

    task2 = BashOperator(
        task_id='print_second',
        bash_command='echo "Привет AirFlow — второй DAG!"'
    )
