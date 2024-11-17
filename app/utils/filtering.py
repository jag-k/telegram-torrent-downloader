from telethon import TelegramClient
from telethon.tl.types import User

from app.config import logger, settings

from .cache import async_lru_cache


__all__ = ("filter_bot_sender",)


def if_bot_is_listening(bot_name: str) -> bool:
    if settings.listen_to is False:
        return True
    elif settings.listen_to is True:
        return bot_name in settings.bot_to_path
    else:
        return bot_name in settings.listen_to


@async_lru_cache()
async def filter_bot_sender(client: TelegramClient, sender_id: int) -> bool:
    try:
        sender = await client.get_entity(sender_id)
    except ValueError:
        logger.warning(f"Could not get sender with ID {sender_id}")
        return False
    if not isinstance(sender, User) or not sender.bot:
        return False
    return if_bot_is_listening(sender.username)
