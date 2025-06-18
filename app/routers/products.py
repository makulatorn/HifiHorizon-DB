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
                    "garanti": p.specs.garanti if p.specs else None,
                    "hastighed": p.specs.hastighed if p.specs else None,
                    "motor": p.specs.motor if p.specs else None,
                    "pickup": p.specs.pickup if p.specs else None,
                    "tone_arm": p.specs.tone_arm if p.specs else None,
                    "plade_tallerken": p.specs.plade_tallerken if p.specs else None,
                    "drev": p.specs.drev if p.specs else None,
                    "kabinett": p.specs.kabinett if p.specs else None,
                    "hastigheder": p.specs.hastigheder if p.specs else None,
                    "frekvensomraade": p.specs.frekvensomraade if p.specs else None,
                    "roer": p.specs.roer if p.specs else None,
                    "effekt": p.specs.effekt if p.specs else None,
                    "foelsomhed": p.specs.foelsomhed if p.specs else None,
                    "impedans": p.specs.impedans if p.specs else None,
                    "type": p.specs.type if p.specs else None,
                    "enheder": p.specs.enheder if p.specs else None,
                    "kontrol": p.specs.kontrol if p.specs else None,
                    "kanaler": p.specs.kanaler if p.specs else None
                } if p.specs else {}
            } for p in products
        ]
    except Exception as e:
        logger.error(f"Database error: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Database error: {str(e)}"
        )