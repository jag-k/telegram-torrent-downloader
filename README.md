# Telegram Torrent Downloader

[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![License](https://img.shields.io/github/license/jag-k/telegram-torrent-downloader)](https://github.com/jag-k/telegram-torrent-downloader/blob/main/LICENCE)
[![GitHub Sponsors](https://img.shields.io/github/sponsors/jag-k)](https://github.com/sponsors/jag-k)

A Telegram "bot" that downloads torrents from Telegram.

## Features

- Download torrents from Telegram to a custom directory per bot

## Installation

Before running the application, you need to create a `.env` file. You can use the [.env.example](.env.example) file as a template.

```shell
cp .env.example .env
nano .env
```

Full configuration options can be found in the [Configuration](Configuration.md) documentation.

### Docker

Via docker run:

```bash
docker pull ghrc.io/jag-k/telegram-torrent-downloader:latest

docker run -d \
    --name telegram-torrent-downloader \
    -e API_ID=YOUR_API_ID \
    -e API_HASH=YOUR_API_HASH \
    -e DOWNLOAD_DIR=/app/downloads \
    -v "$(pwd)/session:/app/session" \
    -v "$(pwd)/downloads:/app/downloads" \
    ghrc.io/jag-k/telegram-torrent-downloader:latest
```

Via docker compose:

```yaml
# compose.yaml
services:
  telegram-torrent-downloader:
    image: ghrc.io/jag-k/telegram-torrent-downloader:latest
    environment:
      # API_ID: YOUR_API_ID
      # API_HASH: YOUR_API_HASH
      DOWNLOAD_DIR: /app/downloads
    env_file:
      - .env
    volumes:
      - "./session:/app/session"
      - "./downloads:/app/downloads"
```

Source: [compose.yaml](compose.yaml)

### Manual

This project uses [uv](https://github.com/astral-sh/uv) to manage dependencies and run the application.
Please make sure you have `uv` installed before running the application
([Installation instructions](https://github.com/astral-sh/uv#installation)).

```shell
# Clone the repository
git clone https://github.com/jag-k/telegram-torrent-downloader.git
cd telegram-torrent-downloader

# Install the dependencies
uv sync -no-install-project --no-dev

# Create a .env file
cp .env.example .env
nano .env

# Run the application
uv run main.py
```

## License

This project is licensed under the [MIT Licence](LICENCE).
