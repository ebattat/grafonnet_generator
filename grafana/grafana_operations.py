import requests
import json


class GrafanaOperations:
    """
    This class responsible for Grafana operations
    """
    def __init__(self, grafana_url, api_key, json_dashboard_path):
        self.grafana_url = grafana_url
        self.api_key = api_key
        self.json_dashboard_path = json_dashboard_path
        self.dashboard_data = {}

    def increment_dashboard_version(self):
        """
        This method increases dashboard version
        :return:
        """
        self.dashboard_data["version"] = int(self.dashboard_data["version"]) + 1

    def read_dashboard_json(self):
        """
        This method reads dashboard from json into dictionary
        :return:
        """
        with open(self.json_dashboard_path, 'r') as f:
            self.dashboard_data = json.load(f)

    def write_dashboard_json(self):
        """
        This method write dashboard data into json
        :return:
        """
        with open(self.json_dashboard_path, 'w') as json_file:
            json.dump(self.dashboard_data , json_file, indent=2)

    def override_dashboard(self):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        try:
            response = requests.post(f"{self.grafana_url}/api/dashboards/db", headers=headers, json={"dashboard": self.dashboard_data})

            if response.status_code == 200:
                print(f"Dashboard '{self.dashboard_data['title']}' overridden successfully.")
            else:
                print(f"Failed to override dashboard '{self.dashboard_data['title']}'. Status code: {response.status_code}")

        except requests.exceptions.RequestException as e:
            print(f"Error overriding dashboard '{self.dashboard_data['title']}': {e}")


