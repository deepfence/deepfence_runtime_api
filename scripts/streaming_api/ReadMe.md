## Streaming API

### Prerequisites

- Golang - https://go.dev/doc/install
- git
- ThreatMapper or ThreatStryker management console

### Build

```shell
git clone https://github.com/deepfence/deepfence_runtime_api
cd deepfence_runtime_api/scripts/streaming_api
go build -o streaming-api .
```

### Run

```shell
./streaming-api --help
```

- Streaming hosts
```shell
./streaming-api \
  --management-console-url=deepfence.customer.com \
  --node-type=hosts \
  --deepfence-key=xxxxxx
```

- Stream hosts, run vulnerability scan on every new host
```shell
./streaming-api \
  --management-console-url=deepfence.customer.com \
  --node-type=hosts \
  --deepfence-key=xxxxxx \
  --vulnerability-scan=true
```

- Stream container images, run vulnerability scan on every new container image
```shell
./streaming-api \
  --management-console-url=deepfence.customer.com \
  --node-type=containers-by-image \
  --deepfence-key=xxxxxx \
  --vulnerability-scan=true
```
