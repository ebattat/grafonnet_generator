FROM quay.io/centos/centos:stream9
WORKDIR /app
RUN dnf update -y && \
    dnf install -y git go wget unzip && \
    go install github.com/google/go-jsonnet/cmd/jsonnet@latest && \
    go install -a github.com/jsonnet-bundler/jsonnet-bundler/cmd/jb@latest
CMD ["/bin/sh", "-c", "/root/go/bin/jsonnet -J vendor main.libsonnet > /app/output.json"]