from airflow import DAG
from datetime import datetime, timedelta



default_args = {
    'owner':'moyin',
    'retries':5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id="weather_etl",
    start_date=datetime(year=2024, month=6, day=1, hour=9, minute=0),
    schedule="@daily",
    catchup=True,
    max_active_runs=1,
    render_template_as_native_obj=True
) as dag:
    pass