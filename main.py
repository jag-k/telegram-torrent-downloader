from telethon import TelegramClient
from telethon.events import NewMessage
from telethon.sessions import SQLiteSession

from app.config import APP_NAME, logger, settings
from app.events import file_downloader


client = TelegramClient(
    SQLiteSession(str(settings.session_dir / APP_NAME)),
    settings.api_id,
    settings.api_hash,
)

client.add_event_handler(file_downloader, NewMessage(incoming=True))


def main():
    logger.info("Starting the client...")
    client.start()
    logger.info("Client started")
    logger.info(f"Session path: {settings.session_dir}")
    logger.info(f"Base download path: {settings.download_dir}")
    client.run_until_disconnected()


if __name__ == "__main__":
    main()
