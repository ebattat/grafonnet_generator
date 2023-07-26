from grafana_operations import GrafanaOperations


grafana_operations = GrafanaOperations(grafana_url='',
                                       api_key='',
                                       json_dashboard_path='output.json')

# Update generate grafana dashboard
grafana_operations.read_dashboard_json()
grafana_operations.increment_dashboard_version()
grafana_operations.write_dashboard_json()
grafana_operations.override_dashboard()
