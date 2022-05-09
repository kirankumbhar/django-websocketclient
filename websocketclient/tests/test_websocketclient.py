from unittest.mock import patch

from django.test import TestCase

from websocketclient import __version__
from websocketclient.client import WebSocketClient


def test_version():
    assert __version__ == "0.1.0"


class TestWebScoketClient(TestCase):
    @patch.multiple("websocketclient.client.websocket_config", host="example.com")
    def test_client_should_return_headers_as_tuple_of_list(self):
        ws_client = WebSocketClient(headers={"testkey": "testvalue"})
        assert len(ws_client.headers) == 1

    @patch.multiple(
        "websocketclient.client.websocket_config",
        host="example.com",
        connect_secure=True,
        path="chat",
    )
    def test_client_should_return_secure_url_if_enable_secure_is_true(self):
        ws_client = WebSocketClient()
        assert ws_client.url == "wss://example.com/chat"

    @patch.multiple(
        "websocketclient.client.websocket_config",
        host="example.com",
        connect_secure=False,
        path="chat",
    )
    def test_client_should_return_unsecure_url_if_enable_secure_is_false(self):
        ws_client = WebSocketClient()
        assert ws_client.url == "ws://example.com/chat"

    @patch.multiple(
        "websocketclient.client.websocket_config",
        host="example.com",
        connect_secure=True,
        path="/chat",
    )
    def test_client_should_remove_prepend_slash_from_path(self):
        ws_client = WebSocketClient()
        assert ws_client.url == "wss://example.com/chat"
