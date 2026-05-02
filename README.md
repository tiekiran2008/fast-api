# FastAPI Chat Application

A simple chat application built with FastAPI that echoes messages and stores them in a SQLite database.

## Features

- **Simple Echo Bot** - Messages are echoed back by the bot
- **SQLite Database** - All messages are stored persistently
- **REST API** - Easy-to-use API endpoints
- **HTML UI** - Simple web interface for chatting
- **CORS Enabled** - Works with frontend applications

## Project Structure

```
fastapi/
├── main.py              # FastAPI application
├── database.py          # Database configuration
├── models.py            # SQLAlchemy models
├── Untitled-2.html      # Web UI
├── requirements.txt     # Python dependencies
├── .gitignore          # Git ignore file
└── chat.db             # SQLite database (generated)
```

## Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd fastapi
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Start the FastAPI server**
   ```bash
   uvicorn main:app --reload
   ```

2. **Open the web UI**
   - Navigate to: `Untitled-2.html` in your browser
   - Or visit: `http://127.0.0.1:8000/docs` for Swagger UI

## API Endpoints

### Home
- `GET /` - Server status

### Chat
- `POST /chat` - Send a message
  ```json
  {
    "message": "hello"
  }
  ```

### History
- `GET /history` - Get all chat messages

## Usage Example

**Send a message:**
```bash
curl -X POST http://127.0.0.1:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "hello"}'
```

**Response:**
```json
{
  "id": 1,
  "user_message": "hello",
  "bot_reply": "hello"
}
```

## Database

Chat messages are stored in `chat.db` (SQLite). To view:
- Download [SQLite Browser](https://sqlitebrowser.org/)
- Open `chat.db` file
- View the `chats` table

Or use the API: `http://127.0.0.1:8000/history`

## Technologies Used

- **FastAPI** - Modern web framework
- **SQLAlchemy** - ORM for database
- **SQLite** - Database
- **Uvicorn** - ASGI server

## License

MIT License
