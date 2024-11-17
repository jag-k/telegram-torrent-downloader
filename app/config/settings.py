from pathlib import Path

from platformdirs import user_downloads_path
from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

__all__ = ("Settings", "APP_NAME")

APP_NAME = "telegram-torrent-downloader"


class Settings(BaseSettings):
    """Settings for the application

    More information about api_id and api_hash can be found in the
    [Telethon documentation](https://docs.telethon.dev/en/stable/basic/signing-in.html).
    """

    model_config = SettingsConfigDict(env_file=".env")

    api_id: int = Field(..., description="Telegram App api_id")
    api_hash: str = Field(..., description="Telegram App api_hash")

    session_dir: Path = Field(
        Path.cwd() / "session",
        description="Path to the session directory",
    )

    download_dir: Path = Field(
        user_downloads_path() / APP_NAME,
        description=f"Path to download torrents to. Default: User download folder + {APP_NAME}",
    )

    bot_to_path: dict[str, Path] = Field(
        default_factory=dict,
        description=(
            "Mapping of bot usernames to paths. "
            "If path was relative, then it will be relative to the download_path: "
            "`DOWNLOAD_DIR / BOT_TO_PATH[bot_username]`. "
            "Example: `{'bot_username': '/path/to/bot', 'another_bot': 'another_path'}`"
        ),
    )
    listen_to: list[str] | bool = Field(
        False,
        description=(
            "List of bot usernames to listen to. "
            "You can also set it to True to listen bots only from the BOT_TO_PATH mapping. "
            "By default, it's False (listen to all bots)."
        ),
    )

    # noinspection PyNestedDecorators
    @field_validator("session_dir", "download_dir")
    @classmethod
    def dir_path_validator(cls, v: Path) -> Path:
        v.mkdir(parents=True, exist_ok=True)
        return v
