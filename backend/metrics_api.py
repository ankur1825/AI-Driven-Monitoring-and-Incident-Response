from fastapi import APIRouter
import requests
import pandas as pd
from config import PROMETHEUS_URL

router = APIRouter()

def query_prometheus(query):
    response = requests.get(f"{PROMETHEUS_URL}/api/v1/query", params={"query": query}, verify=False)
    result = response.json().get("data", {}).get("result", [])
    values = [float(entry['value'][1]) for entry in result]
    timestamps = pd.date_range(end=pd.Timestamp.now(), periods=len(values), freq='min')
    return pd.DataFrame({'ds': timestamps, 'y': values})

@router.get("/metrics/cpu")
def cpu_metrics():
    df = query_prometheus("sum(rate(container_cpu_usage_seconds_total[5m]))")
    return df.to_dict(orient='records')

@router.get("/metrics/memory")
def memory_metrics():
    df = query_prometheus("sum(container_memory_usage_bytes)")
    return df.to_dict(orient='records')

@router.get("/metrics/latency")
def latency_metrics():
    df = query_prometheus("avg(rate(http_request_duration_seconds_sum[5m]))")
    return df.to_dict(orient='records')