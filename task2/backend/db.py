from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

# MySQL Configuration
# Format: mysql+pymysql://username:password@host:port/database
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./reviews.db")

# Create engine with appropriate settings
if DATABASE_URL.startswith("mysql"):
    engine = create_engine(DATABASE_URL, pool_pre_ping=True, pool_recycle=3600)
else:
    # SQLite fallback for local development
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    rating = Column(Integer, nullable=False)
    review_text = Column(Text, nullable=False)
    ai_response = Column(Text, nullable=True) # User-facing response
    ai_summary = Column(Text, nullable=True) # Admin summary
    ai_action = Column(Text, nullable=True) # Recommended action
    created_at = Column(DateTime, default=datetime.utcnow)

def init_db():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
