import os

JIRA_URL = os.getenv("JIRA_URL")
JIRA_USER = os.getenv("JIRA_USER")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")
JIRA_PROJECT_KEY = os.getenv("JIRA_PROJECT_KEY")
PROMETHEUS_URL = os.getenv("PROMETHEUS_URL", "https://prometheus.horizonrelevance.com")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")