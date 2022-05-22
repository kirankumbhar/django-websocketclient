# Django Websocketclient

django-websocketclient is a WebSocket client for Django to connect to the WebSocket server and listen to incoming messages in persistent mode

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install django-websocketclient
```
Or using poetry

```bash
poerty add django-websocketclient
```

## Setup

1. Add `websocketclient` to `INSTALLED_APPS` in `settings.py`

```python
INSTALLED_APPS = [
    "django.contrib.admin",
     ...
     ...
    "websocketclient",
]
```

2. Set Host and async message handler path for WebSocket client in `settings.py`. This async handler will be called to process data received over WebSocket connection

```python
WEBSOCKETCLIENT_HOST = "localhost:8000"
WEBSOCKETCLIENT_MESSAGE_HANDLER = "myproject.handlers.message_handler"

```

3. Create `handlers.py` module at the root level of your project module. A typical django structure will looks like this.

```
myproject
├── 
├── myproject
│   ├── __init__.py
│   ├── asgi.py
│   ├── handlers.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
```

4. Define async message handler coroutine under `myproject/myproject/handlers.py`

```python
async def message_handler(message, websocket):
    # process message here
    print(message)
    
    # You can also send the message back to server
    await websocket.send("Message received from client")
```



## Usage
Run manage.py command to connect to websocket server.

```bash
python manage.py runwebsocketclient
```
Optional CLI Arguments

```
usage: manage.py runwebsocketclient [--host HOST] [--path PATH]
  --host HOST   Websocket Server host
  --path PATH   Websocket Server path
```

## Available Settings

| Variable | Type | Description |
| ---------|------|-------------|
| WEBSOCKETCLIENT_HOST | String| Websocket server host to conenct to. Required |
| WEBSOCKETCLIENT_PATH | String | Path part of websocket url. For e.g. `events/` |
| WEBSOCKETCLIENT_AUTH_HEADER | String| Authentication header key. Defaults to "Authorization" |
| WEBSOCKETCLIENT_TOKEN | String | Token for authenticated connection. |
| WEBSOCKETCLIENT_TOKEN_SCHEME | String | Token scheme to be used as a part of token. For e.g. 'bearer' |
| WEBSOCKETCLIENT_CONNECT_SECURE | Boolean | Set True to use `wss://` protocol. Defaults to False |
| WEBSOCKETCLIENT_DISABLE_SSL_VERIFY | Boolean | Set True to disable SSL verification. Defaults to False |

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)