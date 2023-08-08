
import os

from update_versions_in_main_libsonnet import UpdateGrafanaLastValueMappings

main_libsonnet_path = os.environ.get('PERF_MAIN_LIBSONNET_PATH', 'grafonnet_generator/grafana/perf/jsonnet/main.libsonnet')


# Update perf main.libsonnet with last versions
update_grafana_mappings_value = UpdateGrafanaLastValueMappings(main_libsonnet_path=main_libsonnet_path)
last_versions = update_grafana_mappings_value.get_last_elasticsearch_versions()
update_grafana_mappings_value.update_value_mappings_last_versions(last_versions=last_versions)
update_grafana_mappings_value.update_main_libsonnet()

