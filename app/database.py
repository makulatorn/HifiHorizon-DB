from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")
logger.debug(f"Initial DATABASE_URL: {SQLALCHEMY_DATABASE_URL}")

if SQLALCHEMY_DATABASE_URL and SQLALCHEMY_DATABASE_URL.startswith("postgres://"):
    SQLALCHEMY_DATABASE_URL = SQLALCHEMY_DATABASE_URL.replace("postgres://", "postgresql://", 1)
    
logger.debug(f"Processed DATABASE_URL: {SQLALCHEMY_DATABASE_URL}")

# Add SSL requirements for Render
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    echo=True,  # Will log all SQL
    connect_args={
        "sslmode": "require"
    }
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()