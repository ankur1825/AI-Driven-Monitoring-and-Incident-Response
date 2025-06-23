from fastapi import APIRouter, Body
from openai import OpenAI
from config import OPENAI_API_KEY
import os

router = APIRouter()
client = OpenAI(api_key=OPENAI_API_KEY)

def run_rca(payload: dict):
    system_prompt = """
You are a Site Reliability Incident AI Bot. Given logs, traces, metrics, predict probable root cause.
"""

    logs = payload.get("logs", "")
    traces = payload.get("traces", "")
    metrics = payload.get("metrics", "")

    full_prompt = f"""
Incident Context:
Metrics: {metrics}
Logs: {logs}
Traces: {traces}

{system_prompt}
"""

    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": full_prompt}
        ]
    )

    return {"rca": completion.choices[0].message.content}

# Expose as FastAPI route
@router.post("/generate")
def generate_rca(payload: dict = Body(...)):
    return run_rca(payload)
