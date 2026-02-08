# Image Sharing

## Getting Started

### Prerequisites

- Python 3.14+
- [uv](https://docs.astral.sh/uv/) package manager

### Initialize the Project

```bash
uv init .
```

### Install Dependencies

```bash
uv add fastapi
uv add python-dotenv
uv add "fastapi-users[sqlalchemy]"
uv add imagekitio
uv add "uvicorn[standard]"
uv add aiosqlite
```

Or install all at once:

```bash
uv add fastapi python-dotenv "fastapi-users[sqlalchemy]" imagekitio "uvicorn[standard]" aiosqlite
```

### Run the Server

```bash
uv run uvicorn app.main:app --reload
```
