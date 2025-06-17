from pydantic import BaseModel
from typing import Optional, Dict

class SpecBase(BaseModel):
    dimensioner: Optional[str] = None
    vaegt: Optional[str] = None
    udgange: Optional[str] = None
    stroemforbrug: Optional[str] = None
    fjernbetjening: Optional[str] = None
    skaerm: Optional[str] = None
    dac: Optional[str] = None
    formater: Optional[str] = None
    finish: Optional[str] = None
    garanti: Optional[str] = None
    
    class Config:
        from_attributes = True 

class ProductBase(BaseModel):
    productname: str
    kategori: str
    producent: str
    color: str
    pris: float
    stock: int
    desc: str
    image: str
    specs: Dict[str, Optional[str]]  

class ProductCreate(ProductBase):
    id: str

class Product(ProductBase):
    id: str
    
    class Config:
        from_attributes = True