from fastapi import APIRouter
import requests
import pandas as pd
from prophet import Prophet
from config import PROMETHEUS_URL

router = APIRouter()

@router.get("/cpu")
def predict_cpu():
    query = 'sum(rate(container_cpu_usage_seconds_total[5m]))'
    response = requests.get(f"{PROMETHEUS_URL}/api/v1/query", params={'query': query})
    result = response.json().get('data', {}).get('result', [])

    if not result:
        return {"error": "No CPU data found"}

    values = [float(entry['value'][1]) for entry in result]
    timestamps = pd.date_range(end=pd.Timestamp.now(), periods=len(values), freq='min')

    df = pd.DataFrame({'ds': timestamps, 'y': values})
    model = Prophet()
    model.fit(df)

    future = model.make_future_dataframe(periods=5, freq='min')
    forecast = model.predict(future)

    return forecast[['ds', 'yhat']].tail().to_dict(orient='records')