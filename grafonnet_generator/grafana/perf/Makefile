# jsonnet/jsonnetfile.lock.json - for working on specific grafonnet version
apply:
	@cd jsonnet/ && \
		/root/go/bin/jb install && \
		cd ../ && \
		ls -l && \
		ls -l jsonnet && \
		#terraform apply -auto-approve | python3 extract_dashboard.py > dashboard.json
		/root/go/bin/jsonnet -J jsonnet/vendor jsonnet/main.libsonnet
