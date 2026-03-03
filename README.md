# RomM Client for Decky Loader

> **AI-Generated Project** — This entire project (plugin code, backend, tests, build scripts, and documentation) was generated with the assistance of AI (GitHub Copilot / Claude). All code should be reviewed before use in production. I just wanted a simple way to import roms from my RomM server, and this works good enough. 

A [Decky Loader](https://github.com/SteamDeckHomebrew/decky-loader) plugin that lets you browse and download ROMs from your [RomM](https://github.com/rommapp/romm) server directly on your Steam Deck.

## Features

- **Browse** your RomM library — search ROMs by name across all platforms
- **Download** ROMs directly to your Steam Deck with one tap
- **Automatic zip extraction** — multi-file ROMs that arrive as zips are extracted automatically
- **Per-platform paths** — configure where ROMs for each platform are saved
- **Cover art** — ROM cards display cover images from your RomM server

## RomM OpenAPI SDK

This plugin uses a Python API client generated from the [RomM](https://github.com/rommapp/romm) OpenAPI specification. The client lives in [`rom-m-api-client/`](rom-m-api-client/) and was generated with [openapi-python-client](https://github.com/openapi-generators/openapi-python-client).

| Detail | Value |
|---|---|
| **Package** | `rom-m-api-client` v4.6.1 |
| **Python** | ≥ 3.10 |
| **HTTP library** | [httpx](https://www.python-httpx.org/) `>=0.23.0,<0.29.0` |
| **Serialization** | [attrs](https://www.attrs.org/) `>=22.2.0` |

The SDK provides both **sync** and **async** methods for every endpoint. The plugin backend ([`main.py`](main.py)) uses a thin wrapper ([`py_modules/romm_client.py`](py_modules/romm_client.py)) to authenticate and call the SDK from within the Decky Python sandbox.

For full SDK usage details, see [rom-m-api-client/README.md](rom-m-api-client/README.md).

## Setup

### Prerequisites

- A running [RomM](https://github.com/rommapp/romm) server accessible from your Steam Deck
- [Decky Loader](https://github.com/SteamDeckHomebrew/decky-loader) installed on your Steam Deck

### Configuration

1. Open the plugin from the Decky sidebar
2. Go to **Settings** and enter your RomM server URL, username, and password
3. Go to **Platform Paths** to configure where ROMs for each platform should be saved
4. Go to **ROM Library** to search and download ROMs

## Development

### Dependencies

- Node.js v16.14+
- pnpm v9 (`sudo npm i -g pnpm@9`)
- Python 3.10+ (for backend and tests)

### Build

```bash
pnpm i
pnpm run build
```

Or use the VS Code tasks: `setup` → `build`.

### Test

```bash
# All tests (frontend + Python)
pnpm test
cd rom-m-api-client && python3 -m pytest tests/ -v -m 'not integration'

# Or via VS Code task:
# "test" runs both in parallel
```

### Deploy

- **Remote Steam Deck**: Use the `builddeploy` VS Code task (configure `.vscode/settings.json` with your Deck's IP, user, password)
- **Local (WSL2/desktop)**: Use the `builddeploy:local` VS Code task

## License

BSD-3-Clause
