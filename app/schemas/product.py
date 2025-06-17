from pydantic import BaseModel
from typing import List, Union

class SpecBase(BaseModel):
    key: str
    value: str

class SpecCreate(SpecBase):
    pass

class Spec(SpecBase):
    id: int
    class Config:
        orm_mode = True

class ProductBase(BaseModel):
    id: str
    productname: str
    kategori: str
    producent: str
    color: str
    pris: int
    stock: int
    desc: str
    image: str
    specs: List[SpecCreate] = []

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    class Config:
        orm_mode = True