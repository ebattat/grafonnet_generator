# jsonnet/jsonnetfile.lock.json - for working on specific grafonnet version
apply:
	    cd /app/jsonnet/ && \
		/root/go/bin/jb install && \
		cd ../ && \
		terraform apply -auto-approve | python3 extract_dashboard.py > dashboard.json
