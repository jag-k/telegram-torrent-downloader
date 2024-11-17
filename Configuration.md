# Configuration

Here you can find all available configuration options using ENV variables.

## Settings

Settings for the application

More information about api_id and api_hash can be found in the
[Telethon documentation](https://docs.telethon.dev/en/stable/basic/signing-in.html).

| Name           | Type      | Default                                     | Description                                                                                                                                                                                                                    | Example                                     |
|----------------|-----------|---------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------|
| `API_ID`       | `integer` | `None`                                      | Telegram App api_id                                                                                                                                                                                                            |                                             |
| `API_HASH`     | `string`  | `None`                                      | Telegram App api_hash                                                                                                                                                                                                          |                                             |
| `SESSION_DIR`  | `Path`    | `"<project_dir>/session"`                   | Path to the session directory                                                                                                                                                                                                  | `"<project_dir>/session"`                   |
| `DOWNLOAD_DIR` | `Path`    | `"~/Downloads/telegram-torrent-downloader"` | Path to download torrents to. Default: User download folder + telegram-torrent-downloader                                                                                                                                      | `"~/Downloads/telegram-torrent-downloader"` |
| `BOT_TO_PATH`  | `dict`    | `{}`                                        | Mapping of bot usernames to paths. If path was relative, then it will be relative to the download_path: `DOWNLOAD_DIR / BOT_TO_PATH[bot_username]`. Example: `{'bot_username': '/path/to/bot', 'another_bot': 'another_path'}` | `{}`                                        |
| `LISTEN_TO`    | `list`    | `false`                                     | List of bot usernames to listen to. You can also set it to True to listen bots only from the BOT_TO_PATH mapping. By default, it's False (listen to all bots).                                                                 | `false`                                     |
