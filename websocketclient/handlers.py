import importlib

from django.conf import settings


async def default_message_handler(message, websocket):
    pass


def get_handler_from_settings():
    _handler = getattr(settings, "WEBSOCKETCLIENT_MESSAGE_HANDLER", None)
    if _handler is None:
        return
    if not isinstance(_handler, str):
        return
    handler_module, handler_func_name = _handler.rsplit(".", 1)
    module = importlib.import_module(handler_module)
    handler_func = getattr(module, handler_func_name)
    if handler_func is None:
        return
    return handler_func


message_handler_func = get_handler_from_settings()

if not message_handler_func:
    message_handler_func = default_message_handler
