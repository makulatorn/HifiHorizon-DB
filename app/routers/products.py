from fastapi import APIRouter, Depends, HTTPException, Query
from typing import Optional, Literal
from sqlalchemy.orm import Session
from sqlalchemy import asc, desc
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
async def get_products(
    db: Session = Depends(get_db),
    #Name of what to sort by
    sort_by: Optional[Literal["producent", "color", "pris"]] = Query(
        None,
        description="Sort by:"
    ),
    #Order of sorting
    order: Optional[Literal["asc", "desc"]] = Query(
        "asc",
        description="Sort order: asc (ascending) or desc (descending)"
    ),
    color: Optional[Literal["Sort", "Sølv", "Blå", "Rød", "Gul"]] = Query(
        None,
        description="Filter by color:"
    ),
    producent: Optional[Literal["Creek", "Exposure", "Parasound", "Manley", "Pro-Ject", "Bösendorfer", "Epos", "Harbeth", "Jolida"]] = Query(
        None,
        description="Filter by brand:"
    )
):
    try:
        query = db.query(Product)

        # Apply filters if provided
        if color:
            query = query.filter(Product.color == color)
        if producent:
            query = query.filter(Product.producent == producent)
            
        # Apply sorting
        if sort_by:
            sort_column = getattr(Product, sort_by)
            if order == "desc":
                query = query.order_by(desc(sort_column))
            else:
                query = query.order_by(asc(sort_column))
        
        products = query.all()
        logger.info(f"Found {len(products)} products")
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
        
@router.get("/{product_id}")
async def get_product(product_id: str, db: Session = Depends(get_db)):
    try:
        product = db.query(Product).filter(Product.id == product_id).first()
        if not product:
            raise HTTPException(status_code=404, detail="Not Found")
        return {
            "id": product.id,
            "productname": product.productname,
            "kategori": product.kategori,
            "producent": product.producent,
            "color": product.color,
            "pris": product.pris,
            "stock": product.stock,
            "desc": product.desc,
            "image": product.image,
            "specs": {
                "dimensioner": product.specs.dimensioner if product.specs else None,
                "vaegt": product.specs.vaegt if product.specs else None,
                "udgange": product.specs.udgange if product.specs else None,
                "stroemforbrug": product.specs.stroemforbrug if product.specs else None,
                "fjernbetjening": product.specs.fjernbetjening if product.specs else None,
                "skaerm": product.specs.skaerm if product.specs else None,
                "dac": product.specs.dac if product.specs else None,
                "formater": product.specs.formater if product.specs else None,
                "finish": product.specs.finish if product.specs else None,
                "garanti": product.specs.garanti if product.specs else None,
                "hastighed": product.specs.hastighed if product.specs else None,
                "motor": product.specs.motor if product.specs else None,
                "pickup": product.specs.pickup if product.specs else None,
                "tone_arm": product.specs.tone_arm if product.specs else None,
                "plade_tallerken": product.specs.plade_tallerken if product.specs else None,
                "drev": product.specs.drev if product.specs else None,
                "kabinett": product.specs.kabinett if product.specs else None,
                "hastigheder": product.specs.hastigheder if product.specs else None,
                "frekvensomraade": product.specs.frekvensomraade if product.specs else None,
                "roer": product.specs.roer if product.specs else None,
                "effekt": product.specs.effekt if product.specs else None,
                "foelsomhed": product.specs.foelsomhed if product.specs else None,
                "impedans": product.specs.impedans if product.specs else None,
                "type": product.specs.type if product.specs else None,
                "enheder": product.specs.enheder if product.specs else None,
                "kontrol": product.specs.kontrol if product.specs else None,
                "kanaler": product.specs.kanaler if product.specs else None
            } if product.specs else {}
        }
    except Exception as e:
        logger.error(f"Database error: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Database error: {str(e)}"
        )