from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
import pendulum

local_tz = pendulum.timezone("Asia/Seoul")

DEFAULT_ARGS = {
    'owner': 'levi.y',
    'depends_on_past': False,
    'email': ['levi.y@kakaocorp.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'start_date': datetime(2024, 8, 24, tzinfo=local_tz),
    'retries': 3,
    'retry_delay': timedelta(seconds=20),
    'provide_context': True,
}

with DAG(
    dag_id='sample',
    default_args=DEFAULT_ARGS,
    schedule_interval=None,
    tags=['sample'],
    max_active_runs=1
) as dag:
    wf_start=BashOperator(
        task_id='wf_start',
        bash_command='echo wf_start',
    )
    wf_start