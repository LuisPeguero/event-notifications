# Event Notifications Project

## Overview
Event Notifications Project is a FastAPI-based application for managing events. It includes endpoints for creating, updating, and retrieving events. The application also uses Celery for background task processing and Flower for monitoring Celery tasks.

## Prerequisites
- Docker
- Docker Compose

## Setup and Running

1. **Clone the repository:**
    ```sh
    git clone https://github.com/LuisPeguero/event-notifications.git
    ```

2. **Build and run the Docker containers:**
    ```sh
    docker-compose up --build
    ```

3. **Access the application:**
    - The API will be available at: `http://localhost:5000`
    - Flower UI will be available at: `http://localhost:5555`

## API Documentation
The API documentation is available at `http://localhost:5000/docs`. This documentation provides details on all available endpoints and their usage.

## Flower UI
Flower is a web-based tool for monitoring and administrating Celery clusters. It provides real-time monitoring, task progress, and history. You can access the Flower UI at `http://localhost:5555`.

## Environment Variables
The following environment variables are used in the project and can be configured in the `docker-compose.yml` file:

- `REDIS_PORT`: Port for Redis (default: 6379)
- `REDIS_HOST`: Host for Redis (default: redis)
- `LOG_LEVEL`: Logging level (default: INFO)
- `EVENT_SERVICE_URL`: URL for the event service (default: http://event_logger:5000)

## Logging
Logs are stored in the `info.log` file in the project root directory.


## Running Tests

Test run automatically on Docker image build.