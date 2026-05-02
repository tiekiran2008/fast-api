from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import engine, SessionLocal
from models import Base, Chat
import threading

# Create tables in background thread (non-blocking)
def init_db():
    Base.metadata.create_all(bind=engine)

threading.Thread(target=init_db, daemon=True).start()

app = FastAPI(title="FastAPI Chat System")

# Enable CORS to allow requests from HTML file
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models
class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    id: int
    user_message: str
    bot_reply: str

    class Config:
        from_attributes = True

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "Chat Server running", "status": "online"}

@app.post("/chat", response_model=ChatResponse)
def chat(data: ChatRequest, db: Session = Depends(get_db)):
    user_msg = data.message
    
    # Echo back the same message
    bot_reply = user_msg

    try:
        # Save to database
        new_chat = Chat(user_message=user_msg, bot_reply=bot_reply)
        db.add(new_chat)
        db.commit()
        db.refresh(new_chat)
        return new_chat
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

@app.get("/history", response_model=list[ChatResponse])
def get_history(db: Session = Depends(get_db)):
    chats = db.query(Chat).all()
    return chats

