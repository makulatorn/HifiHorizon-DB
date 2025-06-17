import json
import sys
import os 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.crud import product as crud
from app.schemas.product import ProductCreate
from app.database import SessionLocal

with open("data.json", encoding="utf-8") as f:
    raw_data = json.load(f)
    
def normalize_kategori(kategori):
    return kategori.lower().replace(" ","_").replace(".","").replace("æ","ae").replace("ø","oe").replace("å","aa")

db = SessionLocal()
for entry in raw_data:
    img_subfolder = normalize_kategori(entry["kategori"])
    image_path = f"/static/{img_subfolder}/{entry['image']}"
    #laver et "bibliotek" af data. Giver par ("dimension", "data")
    #laver et ProductCreate object med key=k og value=v
    specs = [{"key": k, "value": v} for k, v in entry["specs"].items()]
    product = ProductCreate(
        id=entry["id"],
        productname=entry["productname"],
        kategori=entry["kategori"],
        producent=entry["producent"],
        color=entry["color"],
        pris=entry["pris"],
        stock=entry["stock"],
        desc=entry["desc"],
        image=image_path,
        specs=specs
    )
    crud.create_product(db, product)
db.close()
