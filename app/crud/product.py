from sqlalchemy.orm import Session
from ..models.product import Product, Spec
from ..schemas.product import ProductCreate

def get_products(db: Session):
    return db.query(Product).all()

def create_product(db: Session, product: ProductCreate):
    db_product = Product(
        id=product.id,
        productname=product.productname,
        kategori=product.kategori,
        producent=product.producent,
        color=product.color,
        pris=product.pris,
        stock=product.stock,
        desc=product.desc,
        image=product.image
    )
    db.add(db_product)
    
    for spec in product.specs:
        db_spec = Spec(
            key=spec.key,
            value=spec.value,
            product_id=db_product.id
        )
        db.add(db_spec)
    
    db.commit()
    db.refresh(db_product)
    return db_product