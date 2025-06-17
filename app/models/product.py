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