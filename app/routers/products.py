from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..models.product import Product
from ..database import SessionLocal
import logging

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
        print(f"Found {len(products)} products")
        
        if not products:
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
                "specs": [
                    {
                        "key": spec.key,
                        "value": spec.value
                    } for spec in p.specs
                ]
            } for p in products
        ]
    except Exception as e:
        print(f"Error: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Database error: {str(e)}"
        )