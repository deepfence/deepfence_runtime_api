### Build image to test
```bash
docker build -t "deepfenceio/deepfence_test_api" .
```

### Test
```bash
docker run --rm -it -v ${PWD}:/tmp --name=deepfence_test_api deepfenceio/deepfence_test_api python /app/test_api.py
docker run --rm -it -v ${PWD}:/tmp --name=deepfence_test_api deepfenceio/deepfence_test_api python /app/test_api.py "https://122.122.122.122/deepfence/v1.5" "ewkwekeejkvewkgewqux"
```

### Running python directly
```bash
sudo apt-get install python-virtualenv
virtualenv -p python3 test_api_venv
test_api_venv/bin/pip install -r requirements.txt
test_api_venv/bin/python test_api.py
test_api_venv/bin/python test_api.py "https://122.122.122.122/deepfence/v1.5" "ewkwekeejkvewkgewqux"
```

### Testing websocket streaming
```bash
docker run --rm -it --name=deepfence_test_api deepfenceio/deepfence_test_api go run /app/websocket_streaming.go -api_url "122.122.122.122" -api_key "ewkwekeejkvewkgewqux" -node_type "host"
```