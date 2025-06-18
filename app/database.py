from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

# Get the database URL and log it for debugging
DATABASE_URL = os.getenv("DATABASE_URL")
logger.info(f"Raw DATABASE_URL: {DATABASE_URL}")

# Ensure the URL exists and format it correctly
if not DATABASE_URL:
    raise ValueError("No DATABASE_URL environment variable set")

# Create the database engine with full connection URL
engine = create_engine(
    DATABASE_URL,
    echo=True,
    pool_pre_ping=True
)

try:
    # Test the connection
    with engine.connect() as conn:
        conn.execute("SELECT 1")
        logger.info("Database connection successful")
except Exception as e:
    logger.error(f"Database connection failed: {str(e)}")
    raise

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()