# jsonnet/jsonnetfile.lock.json - for working on specific grafonnet version
apply:
	@cd jsonnet/ && \
		/root/go/bin/jb install && \
		cd ../ && \
		ls -l && \
		ls -l jsonnet && \
		/root/go/bin/jsonnet -J jsonnet/vendor jsonnet/main.libsonnet

