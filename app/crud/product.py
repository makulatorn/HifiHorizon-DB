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
    
    if product.specs:
        db_spec = Spec(
            product_id=db_product.id,
            dimensioner=product.specs.get("dimensioner"),
            vaegt=product.specs.get("vaegt"),
            udgange=product.specs.get("udgange"),
            stroemforbrug=product.specs.get("stroemforbrug"),
            fjernbetjening=product.specs.get("fjernbetjening"),
            skaerm=product.specs.get("skaerm"),
            dac=product.specs.get("dac"),
            formater=product.specs.get("formater"),
            finish=product.specs.get("finish"),
            garanti=product.specs.get("garanti")
        )
        db.add(db_spec)
    
    db.commit()
    db.refresh(db_product)
    return db_product