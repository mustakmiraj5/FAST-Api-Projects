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

### Option 1: Using Virtual Environment (Recommended for Development)

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

### Option 2: Using Docker (Recommended for Production)

```bash
# Navigate to project directory
cd fundamentals

# Build Docker image
docker build -t fastapi-test .

# Run Docker container
docker run --rm -p 8000:8000 fastapi-test
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
├── .venv/            # Virtual environment (not included in Docker)
├── Dockerfile        # Docker configuration for containerization
├── main.py           # Main application file
├── requirements.txt  # Project dependencies
└── README.md         # This file
```

## Docker Deployment

You can run this application using Docker, which packages the application and all its dependencies into a container.

### Prerequisites for Docker

- Docker installed on your system ([Download Docker](https://www.docker.com/get-started))

### Building the Docker Image

Build the Docker image with the following command:

```bash
docker build -t fastapi-test .
```

**What this command does:**
- `docker build` - Builds a Docker image from the Dockerfile
- `-t fastapi-test` - Tags the image with the name "fastapi-test"
- `.` - Uses the current directory as the build context

**The build process:**
1. Uses Python 3.11-slim as the base image
2. Sets up the working directory as `/app`
3. Copies and installs dependencies from `requirements.txt`
4. Copies the application code (`main.py`) and environment file (`.env`)
5. Exposes port 8000
6. Sets the default command to run uvicorn

### Running the Docker Container

Once the image is built, run the container:

```bash
docker run --rm -p 8000:8000 fastapi-test
```

**Command breakdown:**
- `docker run` - Creates and starts a new container
- `--rm` - Automatically removes the container when it stops
- `-p 8000:8000` - Maps port 8000 from the container to port 8000 on your host machine
- `fastapi-test` - The name of the image to run

**Running in detached mode (background):**

```bash
docker run -d --rm -p 8000:8000 --name my-fastapi-app fastapi-test
```

- `-d` - Runs the container in detached mode (background)
- `--name my-fastapi-app` - Assigns a name to the container

**Overriding environment variables:**

You can override environment variables without rebuilding the image:

```bash
docker run --rm -p 8000:8000 -e APP_NAME="Custom App Name" fastapi-test
```

Or use an environment file:

```bash
docker run --rm -p 8000:8000 --env-file .env fastapi-test
```

### Managing Docker Containers

**View running containers:**
```bash
docker ps
```

**Stop a running container:**
```bash
docker stop my-fastapi-app
```

**View container logs:**
```bash
docker logs my-fastapi-app
```

**View logs in real-time:**
```bash
docker logs -f my-fastapi-app
```

### Docker vs Virtual Environment

**Use Docker when:**
- You want consistent environments across different machines
- Deploying to production servers
- Sharing the application with team members
- You need complete isolation including system dependencies

**Use Virtual Environment when:**
- Developing locally and making frequent code changes
- You want faster iteration (no rebuild needed)
- You prefer direct access to Python debugging tools

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

**For virtual environment:**
```bash
uvicorn main:app --port 8001 --reload
```

**For Docker:**
```bash
docker run --rm -p 8001:8000 fastapi-test
```
Note: The format is `-p <host-port>:<container-port>`, so 8001 on your machine maps to 8000 in the container.

### Module Not Found Error

Ensure your virtual environment is activated and all dependencies are installed:

```bash
source .venv/bin/activate  # On macOS/Linux
pip install -r requirements.txt
```

### Docker Image Not Building

If the Docker build fails:
1. Ensure Docker is running: `docker ps`
2. Check that all required files exist (Dockerfile, requirements.txt, main.py, .env)
3. Try rebuilding without cache: `docker build --no-cache -t fastapi-test .`

### Docker Container Not Accessible

If you can't access the application at localhost:8000:
1. Check if the container is running: `docker ps`
2. Verify port mapping is correct: `-p 8000:8000`
3. Check container logs: `docker logs <container-id>`
4. Ensure no other service is using port 8000

## Next Steps

- Add more endpoints and functionality
- Implement request validation using Pydantic models
- Add database integration
- Implement authentication and authorization
- Write unit tests
