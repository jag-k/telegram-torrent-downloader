from pathlib import Path
from typing import TYPE_CHECKING

from telethon import events
from telethon.tl.types import DocumentAttributeFilename, MessageMediaDocument, User

from app.config import logger, settings
from app.utils import filter_bot_sender


if TYPE_CHECKING:
    from telethon.tl.custom import Message


__all__ = ("file_downloader",)


def get_download_dir(sender_name: str) -> Path:
    download_dir = settings.bot_to_path.get(sender_name, settings.download_dir / sender_name)

    if not download_dir.is_absolute():
        download_dir = settings.download_dir / download_dir

    download_dir.mkdir(parents=True, exist_ok=True)
    return download_dir


async def file_downloader(event: events.NewMessage.Event) -> None:
    message: Message = event.message

    # Filter out messages from bots we don't want to listen to
    if not await filter_bot_sender(event.client, message.sender_id):
        return

    # Filter out messages that aren't torrents
    media = message.media
    if (
        not message.media
        or not isinstance(media, MessageMediaDocument)
        or media.document.mime_type != "application/x-bittorrent"
    ):
        return

    # Get the download directory for the sender
    sender: User = await event.get_sender()
    sender_name = sender.username
    download_dir = get_download_dir(sender_name)

    # Check if a file already exists
    for attr in media.document.attributes:
        if isinstance(attr, DocumentAttributeFilename):
            download_path = download_dir / attr.file_name
            if download_path.exists():
                logger.info(f"File `{download_path}` from @{sender_name} already exists. Skipping...")
                return
            break

    # Download the file
    download_path = await message.download_media(download_dir)
    logger.info(f"Downloaded `{download_path}` file from @{sender_name}")
