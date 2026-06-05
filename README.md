# Student Task Manager REST API

A RESTful API built with Python and Flask for managing student tasks. Supports full CRUD operations with SQLite database storage.

## Features
- 5 REST API endpoints (GET, POST, PUT, DELETE)
- Persistent SQLite database storage
- JSON request and response handling
- Error handling with proper HTTP status codes
- Tested using Postman and PowerShell

## Tech Stack
- Python 3.14
- Flask 3.1.3
- SQLite
- Werkzeug

## Project Structure
- `main.py` — main server file with all API endpoints
- `database.py` — database connection and initialisation
- `tasks.db` — SQLite database (auto-created on run)

## How to Run
Server runs at: http://127.0.0.1:5000

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /tasks | Get all tasks |
| GET | /tasks/<id> | Get one task |
| POST | /tasks | Create new task |
| PUT | /tasks/<id> | Update a task |
| DELETE | /tasks/<id> | Delete a task |

## Sample Request (POST)
```json
{
  "title": "Complete DSA assignment",
  "description": "Solve 5 linked list problems"
}
```

## Sample Response
```json
{
  "message": "Task created successfully"
}
```
