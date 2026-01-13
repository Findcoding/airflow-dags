from airflow.decorators import dag, task
from datetime import datetime

@dag(
    dag_id="hello_world_taskflow",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
)
def hello_world():

    @task
    def say_hello():
        print("Hello World from Airflow!")

    say_hello()

hello_world()
