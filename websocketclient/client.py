import asyncio
import logging
import sys
from typing import Dict
from typing import List
from typing import Tuple

from django.core.management.base import OutputWrapper
import websockets

from websocketclient.config import websocket_config
from websocketclient.handlers import message_handler_func

logger = logging.getLogger(__name__)


class WebSocketClient:
    def __init__(
        self,
        headers: Dict[str, str] = None,
        stdout: OutputWrapper = None,
    ) -> None:
        self.stdout: OutputWrapper = stdout if stdout else OutputWrapper(sys.stdout)
        self.__host: str = websocket_config.host
        self.__path: str = websocket_config.path
        self.__headers: Dict[str, str] = headers if headers else {}
        self.__protocol = "wss" if websocket_config.connect_secure else "ws"
        if websocket_config.token:
            token_value = websocket_config.token
            if websocket_config.token_scheme:
                token_value = f"{websocket_config.token_scheme} {token_value}"
            self.__headers[websocket_config.auth_header] = token_value
        self.__connection_options = {
            "extra_headers": self.headers,
        }
        if websocket_config.connect_secure:
            self.__connection_options["ssl"] = (
                False if websocket_config.disable_ssl_verify else True
            )

    @property
    def host(self) -> str:
        return self.__host

    @host.setter
    def host(self, value):
        self.__host = value

    @property
    def path(self) -> str:
        return self.__path

    @path.setter
    def path(self, value):
        self.__path = value

    @property
    def headers(self) -> List[Tuple]:
        return [(k, v) for k, v in self.__headers.items()]

    @property
    def url(self):
        path = self.__path
        if path.startswith("/"):
            path = path[1:]
        return f"{self.__protocol}://{self.__host}/{path}"

    def run(self):
        asyncio.run(self.connect())

    async def connect(self):
        async for websocket in websockets.connect(
            self.url, **self.__connection_options
        ):
            self.stdout.write("Successfully connected to Websocket Server")
            try:
                async for message in websocket:
                    await self.process_message(message, websocket)
            except websockets.ConnectionClosed:
                logger.error(f"Websocket connection to {self.url} lost! Retrying...")
                continue
            except Exception as e:
                msg = f"Websocket connection to {self.url} failed."
                logger.error(f"{msg} Error: {str(e)}")
                raise Exception(msg)

    async def process_message(self, message, websocket):
        await message_handler_func(message, websocket)
