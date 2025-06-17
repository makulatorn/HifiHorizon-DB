from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base  # Changed from ..database import Base

# ...existing code...

class Spec(Base):
    __tablename__ = "specs"
    
    id = Column(Integer, primary_key=True, index=True)
    key = Column(String)
    value = Column(String)
    product_id = Column(String, ForeignKey("products.id"))
    
    product = relationship("Product", back_populates="specs")

class Product(Base):
    __tablename__ = "products"
    
    id = Column(String, primary_key=True, index=True)
    productname = Column(String, index=True)
    kategori = Column(String)
    producent = Column(String)
    color = Column(String)
    pris = Column(Integer)
    stock = Column(Integer)
    desc = Column(String)
    image = Column(String)
    
    specs = relationship("Spec", back_populates="product")