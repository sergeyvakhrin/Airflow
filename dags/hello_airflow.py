from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from datetime import datetime


def hello_world():
    print("Hello World Airflow!!!")


default_args = {
    'start_date': datetime(2025, 7, 26),
}

with DAG(
    dag_id='my_daily_dag',
    default_args=default_args,
    schedule_interval='1 * * * *',
    catchup=False
) as dag:

    say_hello = BashOperator(
        task_id='print_hello',
        bash_command='echo "Привет AirFlow"'
    )

    second_task = BashOperator(
        task_id='print_second',
        bash_command='echo "Вторая задача выполнена!"'
    )

    task_3 = PythonOperator(
        task_id='python_operator',
        python_callable=hello_world
    )

    # Запускаем второй DAG
    trigger_second_dag = TriggerDagRunOperator(
        task_id='trigger_second_dag',
        trigger_dag_id='second_dag',
    )

    say_hello >> (second_task, task_3) >> trigger_second_dag
