from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.base import Base  # Updated import path
import os
from dotenv import load_dotenv

# ...existing code...

load_dotenv()

if not os.getenv("DATABASE_URL"):
    raise ValueError("DATABASE_URL environment variable is not set")

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)