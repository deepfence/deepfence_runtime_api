# Deepfence Streaming API

Streaming API provide live updates of topology changes (hosts, containers, processes, pods)

### Setup

```bash
pip install git+git://github.com/deepfence/engineio-client-deepfence#egg=engineio-client-deepfence
pip install git+git://github.com/deepfence/socketio-client-deepfence#egg=socketio-client-deepfence
```

### Example
```python
from __future__ import print_function
import gevent

from gevent import monkey

monkey.patch_socket()
monkey.patch_ssl()
from socketio_client_deepfence.manager import Manager

node_type = "host"
"""
Different node types: host, container, process, pod
"""
api_url = "123.123.123.123"
api_port = 443
api_key = ""
io = Manager("https", api_url, api_port, auto_connect=True, ssl_verify=False,
             params={"api_key": api_key})
socketio = io.socket('/websockets')

@socketio.on(node_type)
def on_node_data(*args, **kwargs):
    print(node_type)
    print("Received ", node_type)
    print(args)

@socketio.on_connect()
def on_connect():
    print("Websocket connected")

@socketio.on("established")
def on_established(*args, **kwargs):
    print("Connection established")
    print(args)
    socketio.emit("join", {"channel": node_type})

socketio.connect()
gevent.wait()
```

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

