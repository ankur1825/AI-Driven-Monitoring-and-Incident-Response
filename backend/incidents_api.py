from fastapi import APIRouter
import requests
from requests.auth import HTTPBasicAuth
from config import JIRA_URL, JIRA_USER, JIRA_API_TOKEN

router = APIRouter()

@router.get("/incidents")
def get_incidents():
    url = f"{JIRA_URL}/rest/api/3/search"
    jql = "project = INC AND statusCategory != Done ORDER BY created DESC"
    headers = {"Content-Type": "application/json"}
    auth = HTTPBasicAuth(JIRA_USER, JIRA_API_TOKEN)

    response = requests.get(url, headers=headers, auth=auth, params={"jql": jql})
    issues = response.json().get("issues", [])

    results = []
    for issue in issues:
        results.append({
            "key": issue["key"],
            "summary": issue["fields"]["summary"],
            "status": issue["fields"]["status"]["name"],
            "url": f"{JIRA_URL}/browse/{issue['key']}"
        })

    return results