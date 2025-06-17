from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..models.product import Product
from ..database import SessionLocal
import logging
import os

# Create logs directory if it doesn't exist
os.makedirs('logs', exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/app.log'),  # Log to file
        logging.StreamHandler()  # Log to console
    ]
)
logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/products",
    tags=["products"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
async def get_products(db: Session = Depends(get_db)):
    try:
        products = db.query(Product).all()
        logger.info(f"Found{len(products)} products")
        
        if not products:
            logger.warning("No products found in database")
            raise HTTPException(
                status_code=404, 
                detail="No products found in database"
            )
            
        return [
            {
                "id": p.id,
                "productname": p.productname,
                "kategori": p.kategori,
                "producent": p.producent,
                "color": p.color,
                "pris": p.pris,
                "stock": p.stock,
                "desc": p.desc,
                "image": p.image,
                "specs": {
                    "dimensioner": p.specs.dimensioner if p.specs else None,
                    "vaegt": p.specs.vaegt if p.specs else None,
                    "udgange": p.specs.udgange if p.specs else None,
                    "stroemforbrug": p.specs.stroemforbrug if p.specs else None,
                    "fjernbetjening": p.specs.fjernbetjening if p.specs else None,
                    "skaerm": p.specs.skaerm if p.specs else None,
                    "dac": p.specs.dac if p.specs else None,
                    "formater": p.specs.formater if p.specs else None,
                    "finish": p.specs.finish if p.specs else None,
                    "garanti": p.specs.garanti if p.specs else None
                } if p.specs else {}
            } for p in products
        ]
    except Exception as e:
        logger.error(f"Database error: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Database error: {str(e)}"
        )