# GenAI RCA API
# Full RCA engine connecting your observability data to GenAI.
from fastapi import FastAPI, Body
from openai import OpenAI

app = FastAPI()

client = OpenAI(api_key="your-openai-key")

@app.post("/rca/generate")
def generate_rca(payload: dict = Body(...)):
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
