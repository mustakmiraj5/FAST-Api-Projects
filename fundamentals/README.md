# FastAPI Fundamentals

A basic FastAPI application demonstrating fundamental concepts including API endpoints, path parameters, and environment configuration.

## Project Overview

This project contains a simple FastAPI server with two endpoints:
- `/ping` - Health check endpoint
- `/greet/{name}` - Personalized greeting endpoint

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package manager)

## Quick Start

```bash
# Navigate to project directory
cd fundamentals

# Create virtual environment
python -m venv .venv

# Activate virtual environment
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Visit [http://localhost:8000/docs](http://localhost:8000/docs) to see the interactive API documentation.

## Installation

### 1. Navigate to the project directory

```bash
cd fundamentals
```

### 2. Create a virtual environment

A virtual environment is an isolated Python environment that keeps dependencies required by this project separate from your global Python installation.

**Why use a virtual environment?**
- Prevents dependency conflicts between different projects
- Keeps your global Python installation clean
- Makes it easy to reproduce the exact environment on another machine
- Allows different projects to use different versions of the same package

**Create the virtual environment:**
```bash
python -m venv .venv
```

**What this command does:**
- `python -m venv` - Runs Python's built-in venv module
- `.venv` - Creates a directory named `.venv` containing the virtual environment

**The `.venv` folder will contain:**
- A copy of the Python interpreter
- pip (package installer)
- A lib directory for installed packages
- Scripts/bin directory for executables

### 3. Activate the virtual environment

After creating the virtual environment, you need to activate it. This tells your terminal to use the Python interpreter and packages from the virtual environment instead of the global installation.

**On macOS/Linux:**
```bash
source .venv/bin/activate
```

**On Windows:**
```bash
.venv\Scripts\activate
```

**You'll know it's activated when you see** `(.venv)` **at the beginning of your terminal prompt.**

### 4. Install dependencies

With the virtual environment activated, install all required packages:

```bash
pip install -r requirements.txt
```

This reads the `requirements.txt` file and installs all listed packages into your virtual environment.

**Note:** Always activate the virtual environment before installing packages or running the server.

## Environment Configuration

The application uses environment variables for configuration. A `.env` file is already included with the following variable:

```
APP_NAME=My FastAPI Application
```

You can modify this file to customize the application name or add additional environment variables as needed.

## Running the Server

### Development Mode

Start the server with auto-reload enabled (recommended for development):

```bash
uvicorn main:app --reload
```

### Production Mode

Start the server without auto-reload:

```bash
uvicorn main:app
```

### Custom Host and Port

To run on a specific host and port:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

The server will start and be accessible at `http://localhost:8000`

## API Endpoints

Once the server is running, you can access the following endpoints:

### Health Check

```
GET http://localhost:8000/ping
```

**Response:**
```json
{
  "message": "pong!",
  "status": "success"
}
```

### Greeting

```
GET http://localhost:8000/greet/{name}
```

**Example:**
```
GET http://localhost:8000/greet/John
```

**Response:**
```json
{
  "message": "Hello, John!",
  "status": "success"
}
```

## Interactive API Documentation

FastAPI automatically generates interactive API documentation:

- **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)

## Dependencies

- **fastapi** (0.115.5) - Modern web framework for building APIs
- **uvicorn[standard]** (0.32.0) - ASGI server for running the application
- **python-dotenv** (1.0.1) - Load environment variables from .env file

## Project Structure

```
fundamentals/
├── .env              # Environment variables
├── .venv/            # Virtual environment
├── main.py           # Main application file
├── requirements.txt  # Project dependencies
└── README.md         # This file
```

## Deactivating the Virtual Environment

When you're done working on the project, you can deactivate the virtual environment:

```bash
deactivate
```

This returns your terminal to using the global Python installation.

## Development Tips

1. **Virtual Environment:** Always ensure your virtual environment is activated before installing packages or running the server
2. **Auto-reload:** Use the `--reload` flag during development to automatically restart the server when code changes are detected
3. **API Testing:** Use the built-in Swagger UI at `/docs` to test your API endpoints interactively
4. **Environment Variables:** Add sensitive information (like API keys, database URLs) to the `.env` file and never commit it to version control
5. **Checking Activation:** Look for `(.venv)` in your terminal prompt to confirm the virtual environment is active

## Troubleshooting

### Port Already in Use

If port 8000 is already in use, specify a different port:

```bash
uvicorn main:app --port 8001 --reload
```

### Module Not Found Error

Ensure your virtual environment is activated and all dependencies are installed:

```bash
source .venv/bin/activate  # On macOS/Linux
pip install -r requirements.txt
```

## Next Steps

- Add more endpoints and functionality
- Implement request validation using Pydantic models
- Add database integration
- Implement authentication and authorization
- Write unit tests
