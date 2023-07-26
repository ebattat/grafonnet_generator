import os

# Access environment variables using os.environ
grafana_url = os.environ.get("GRAFANA_URL")
api_key = os.environ.get("API_KEY")
json_dashboard_path = os.environ.get("JSON_DASHBOARD_PATH", 'output.json')



from grafana_operations import GrafanaOperations


grafana_operations = GrafanaOperations(grafana_url=grafana_url,
                                       api_key=api_key,
                                       json_dashboard_path=json_dashboard_path)

# Update generate grafana dashboard
grafana_operations.read_dashboard_json()
grafana_operations.increment_dashboard_version()
grafana_operations.write_dashboard_json()
grafana_operations.override_dashboard()
