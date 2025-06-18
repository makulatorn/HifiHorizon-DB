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
            garanti=product.specs.get("garanti"),
            hastighed=product.specs.get("hastighed"),
            motor=product.specs.get("motor"),
            pickup=product.specs.get("pickup"),
            tone_arm=product.specs.get("tonearm"),
            plade_tallerken=product.specs.get("pladetallerken"),
            drev=product.specs.get("drev"),
            kabinett=product.specs.get("kabinett"),
            hastigheder=product.specs.get("hastigheder"),
            frekvensomraade=product.specs.get("frekvensområde"),
            roer=product.specs.get("rør"),
            effekt=product.specs.get("effekt"),
            foelsomhed=product.specs.get("følsomhed"),
            impedans=product.specs.get("impedans"),
            type=product.specs.get("type"),
            enheder=product.specs.get("enheder"),
            kontrol=product.specs.get("kontrol"),
            kanaler=product.specs.get("kanaler")
        )
        db.add(db_spec)
    
    db.commit()
    db.refresh(db_product)
    return db_product