terraform {
  required_providers {
    jsonnet = {
      source  = "alxrem/jsonnet"
      version = "2.3.0"
    }
  }
}

provider "jsonnet" {
  jsonnet_path = "jsonnet/vendor"
}

data "jsonnet_file" "dashboard" {
  source = "jsonnet/main.libsonnet"
}

output "dashboard" {
  value = data.jsonnet_file.dashboard.rendered
}
