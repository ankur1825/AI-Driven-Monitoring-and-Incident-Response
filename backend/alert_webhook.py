from fastapi import APIRouter
from models import AlertModel
from rca_backend import run_rca
from jira_integration import create_jira_ticket

router = APIRouter()
alerts_store = []  # in-memory store

@router.post("/webhook")
async def alert_webhook(alert: AlertModel):
    print("🛎️ Alert received:", alert.details)

    try:
        rca_result = run_rca({
            "logs": alert.details, "traces": "", "metrics": ""
        })
        print("✅ RCA result:", rca_result)
    except Exception as e:
        print("❌ RCA generation failed:", e)
        return {"error": "RCA generation failed", "details": str(e)}

    try:
        create_jira_ticket(alert.details, rca_result.get("rca", "No RCA generated"))
        print("✅ Jira ticket created")
    except Exception as e:
        print("❌ Jira creation failed:", e)
        return {"error": "Jira ticket creation failed", "details": str(e)}

    alerts_store.append(alert.dict())  # ✅ save the alert
    return {"status": "OK", "received": alert.details}

@router.get("/")
async def get_alerts():
    return alerts_store
