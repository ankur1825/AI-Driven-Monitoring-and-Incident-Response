from fastapi import FastAPI
import time

# OpenTelemetry imports
import otel_setup
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor

app = FastAPI()

# Instrumentation
FastAPIInstrumentor().instrument_app(app)
RequestsInstrumentor().instrument()

@app.get("/hello")
def hello():
    time.sleep(1)
    return {"message": "Hello from OTEL FastAPI!"}

