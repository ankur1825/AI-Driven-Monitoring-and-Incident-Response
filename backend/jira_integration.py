import requests
from requests.auth import HTTPBasicAuth
from config import JIRA_URL, JIRA_USER, JIRA_API_TOKEN, JIRA_PROJECT_KEY

def create_jira_ticket(alert, rca):
    url = f"{JIRA_URL}/rest/api/3/issue"
    headers = {"Content-Type": "application/json"}
    auth = HTTPBasicAuth(JIRA_USER, JIRA_API_TOKEN)

    payload = {
        "fields": {
            "project": {"key": JIRA_PROJECT_KEY},
            "summary": f"Incident: {alert}",
            "description": rca,
            "issuetype": {"name": "Task"}  # Use "Task", "Bug", or verify "Incident"
        }
    }

    response = requests.post(url, headers=headers, auth=auth, json=payload)

    if response.status_code == 201:
        issue_key = response.json().get("key")
        return {"status": "success", "issue_key": issue_key}
    else:
        return {
            "status": "error",
            "code": response.status_code,
            "message": response.text
        }
