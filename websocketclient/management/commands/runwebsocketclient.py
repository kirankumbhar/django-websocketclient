from django.core.management.base import BaseCommand

from websocketclient.client import WebSocketClient


class Command(BaseCommand):
    help = "Run Websocket Client Service for Django App"

    def __init__(self, websocket_client=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = (
            websocket_client
            if websocket_client
            else WebSocketClient(stdout=self.stdout)
        )

    def add_arguments(self, parser):
        parser.add_argument("--host", type=str, help="Websocket Server host")
        parser.add_argument("--path", type=str, help="Websocket Server path")

    def configure_options(self, **options):
        if options.get("host"):
            self.client.host = options.get("host")
        if not self.client.host:
            raise HostNotSpecifiedError(
                "Configure WEBSOCKETCLIENT_HOST in settings or pass using --host arg."
            )
        if options.get("path"):
            self.client.path = options.get("path")

    def handle(self, *args, **options):
        self.configure_options(**options)
        self.stdout.write(f"Connecting to Websocket Server at {self.client.url}")
        self.client.run()


class HostNotSpecifiedError(Exception):
    pass
