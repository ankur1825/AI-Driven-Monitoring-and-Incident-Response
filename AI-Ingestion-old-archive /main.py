# Ingestion & Forecast API
# Early prediction engine via Prophet. Later we’ll plug better models.
from fastapi import FastAPI
import requests
import numpy as np
import pandas as pd
from prophet import Prophet

app = FastAPI()

PROM_URL = "http://prometheus-server.observability-horizon-relevance.svc.cluster.local:80"

@app.get("/predict/cpu")
def predict_cpu():
    query = 'sum(rate(container_cpu_usage_seconds_total[5m]))'
    response = requests.get(f"{PROM_URL}/api/v1/query", params={'query': query})
    result = response.json()['data']['result']

    timestamps = []
    values = []

    for entry in result:
        timestamps.append(pd.Timestamp.now())
        values.append(float(entry['value'][1]))

    df = pd.DataFrame({'ds': timestamps, 'y': values})
    model = Prophet()
    model.fit(df)

    future = model.make_future_dataframe(periods=5, freq='min')
    forecast = model.predict(future)

    return forecast[['ds','yhat']].tail().to_dict()
