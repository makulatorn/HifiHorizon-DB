from sqlalchemy import text
from app.database import engine, SessionLocal
from app.models.base import Base
from app.models.product import Product, Spec
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def init_db():
    logger.info("Creating database tables...")
    try:
        # Create all tables
        Base.metadata.create_all(bind=engine)
        
        # Verify tables were created
        with engine.connect() as conn:
            result = conn.execute(text("SELECT table_name FROM information_schema.tables WHERE table_schema='public'"))
            tables = [row[0] for row in result]
            logger.info(f"Created tables: {tables}")
            
        logger.info("Database tables created successfully!")
    except Exception as e:
        logger.error(f"Error creating tables: {str(e)}")
        raise

if __name__ == "__main__":
    init_db()