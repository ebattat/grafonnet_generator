import os
from grafana_operations import GrafanaOperations

# Access environment variables using os.environ
grafana_url = os.environ.get('PERF_GRAFANA_URL', '')
api_key = os.environ.get('PERF_GRAFANA_API_KEY', '')
json_dashboard_path = os.environ.get('PERF_GRAFANA_JSON', 'output.json')

grafana_operations = GrafanaOperations(grafana_url=grafana_url,
                                       api_key=api_key,
                                       json_dashboard_path=json_dashboard_path)

# Update generate grafana dashboard
# for debug: grafana_operations.fetch_all_dashboards()
grafana_operations.read_dashboard_json()
grafana_operations.increment_dashboard_version()
grafana_operations.write_dashboard_json()
grafana_operations.override_dashboard()

# Error: 412 - need to find last working index
# The 412 status code is used when a newer dashboard already exists (newer, its version is greater than the version that was sent). The same status code is also used if another dashboard exists with the same title.
