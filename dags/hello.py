from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'datamasterylab',
    'start_date': datetime(2025, 6, 21),
    'catchup': False
    
}