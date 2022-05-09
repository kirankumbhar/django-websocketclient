from django.conf import settings


async def message_handler(message):
    print(message)


message_handler_func = getattr(
    settings, "WEBSOCKETCLIENT_MESSAGE_HANDLER", message_handler
)
