from dataclasses import dataclass

from django.conf import settings


@dataclass
class WebSocketConfig:
    host: str = getattr(settings, "WEBSOCKETCLIENT_HOST", None)
    path: str = getattr(settings, "WEBSOCKETCLIENT_PATH", "")
    auth_header: str = getattr(settings, "WEBSOCKETCLIENT_AUTH_HEADER", "Authorization")
    token: str = getattr(settings, "WEBSOCKETCLIENT_TOKEN", "")
    token_scheme: str = getattr(settings, "WEBSOCKETCLIENT_TOKEN_SCHEME", "")
    connect_secure: bool = getattr(settings, "WEBSOCKETCLIENT_CONNECT_SECURE", False)
    disable_ssl_verify: bool = getattr(
        settings, "WEBSOCKETCLIENT_DISABLE_SSL_VERIFY", False
    )


websocket_config = WebSocketConfig()
