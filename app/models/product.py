from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(String, primary_key=True)
    productname = Column(String)
    kategori = Column(String)
    producent = Column(String)
    color = Column(String)
    pris = Column(Float)
    stock = Column(Integer)
    desc = Column(String)
    image = Column(String)
    specs = relationship("Spec", back_populates="product", uselist=False)

class Spec(Base):
    __tablename__ = "specs"

    id = Column(Integer, primary_key=True)
    product_id = Column(String, ForeignKey("products.id"))
    product = relationship("Product", back_populates="specs")
    dimensioner = Column(String(255), nullable=True)
    vaegt = Column(String(255), nullable=True)
    udgange = Column(String(255), nullable=True)
    stroemforbrug = Column(String(255), nullable=True)
    fjernbetjening = Column(String(255), nullable=True)
    skaerm = Column(String(255), nullable=True)
    dac = Column(String(255), nullable=True)
    formater = Column(String(255), nullable=True)
    finish = Column(String(255), nullable=True)
    garanti = Column(String(255), nullable=True)
    hastighed = Column(String(255), nullable=True)
    motor = Column(String(255), nullable=True)
    pickup = Column(String(255), nullable=True)
    tone_arm = Column(String(255), nullable=True)
    plade_tallerken = Column(String(255), nullable=True)
    drev = Column(String(255), nullable=True)
    kabinett = Column(String(255), nullable=True)
    hastigheder = Column(String(255), nullable=True)
    frekvensomraade = Column(String(255), nullable=True)
    roer = Column(String(255), nullable=True)
    effekt = Column(String(255), nullable=True)
    foelsomhed = Column(String(255), nullable=True)
    impedans = Column(String(255), nullable=True)
    type = Column(String(255), nullable=True)
    enheder = Column(String(255), nullable=True)
    kontrol = Column(String(255), nullable=True)
    kanaler = Column(String(255), nullable=True)