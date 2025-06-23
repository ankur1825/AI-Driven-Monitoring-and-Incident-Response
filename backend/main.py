from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(root_path="/backend") 

# Optional CORS if using from browsers
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://localhost:3000",
        "https://horizonrelevance.com"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Import and include your routers
from rca_backend import router as rca_router
from alert_webhook import router as alert_router
from ml_ingest import router as ml_router
from metrics_api import router as metrics_router
from incidents_api import router as incidents_router
#from jira_integration import router as jira_router  # optional if router exists

app.include_router(rca_router, prefix="/rca")
app.include_router(alert_router, prefix="/api/alerts")
app.include_router(ml_router, prefix="/predict")
app.include_router(metrics_router, prefix="/api")
app.include_router(incidents_router, prefix="/api")
# app.include_router(jira_router)  # if you have this

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/routes")
def list_routes():
    return [route.path for route in app.router.routes]





# from fastapi import FastAPI
# from alert_webhook import router as alert_router
# from rca_backend import router as rca_router
# from ml_ingest import router as ml_router

# app = FastAPI()

# app.include_router(alert_router, prefix="/api/alerts")
# app.include_router(rca_router, prefix="/rca")
# app.include_router(ml_router, prefix="/predict")