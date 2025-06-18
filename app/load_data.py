from sqlalchemy.orm import Session
from .models.product import Product
from .database import SessionLocal
from .schemas.product import ProductCreate
from .crud.product import create_product  # Add this import
import json

def load_data():
    db = SessionLocal()
    try:
        # Read JSON data
        with open("data.json", "r", encoding="utf-8") as f:
            raw_data = json.load(f)

        for entry in raw_data:
            if "kategori" not in entry:
                continue

            # Check if product already exists
            existing_product = db.query(Product).filter(
                Product.id == entry.get("id")
            ).first()
            
            if existing_product:
                print(f"Product {entry.get('id')} already exists, skipping...")
                continue

            # Transform specs if they exist
            if "specs" in entry:
                specs = {
                    "dimensioner": entry["specs"].get("dimensioner"),
                    "vaegt": entry["specs"].get("vægt"),
                    "udgange": entry["specs"].get("udgange"),
                    "indgange": entry["specs"].get("indgange"),
                    "stroemforbrug": entry["specs"].get("strømforbrug"),
                    "fjernbetjening": entry["specs"].get("fjernbetjening"),
                    "skaerm": entry["specs"].get("skærm"),
                    "dac": entry["specs"].get("DAC"),
                    "formater": entry["specs"].get("understøttede formater"),
                    "finish": entry["specs"].get("finish"),
                    "garanti": entry["specs"].get("garanti"),
                    "hastighed": entry["specs"].get("hastighed"),
                    "motor": entry["specs"].get("motor"),
                    "pickup": entry["specs"].get("pickup"),
                    "tone_arm": entry["specs"].get("tonearm"),
                    "plade_tallerken": entry["specs"].get("pladetallerken"),
                    "drev": entry["specs"].get("drev"),
                    "kabinett": entry["specs"].get("kabinett"),
                    "hastigheder": entry["specs"].get("hastigheder"),
                    "frekvensomraade": entry["specs"].get("frekvensområde"),
                    "roer": entry["specs"].get("rør"),
                    "effekt": entry["specs"].get("effekt"),
                    "foelsomhed": entry["specs"].get("følsomhed"),
                    "impedans": entry["specs"].get("impedans"),
                    "type": entry["specs"].get("type"),
                    "enheder": entry["specs"].get("enheder"),
                    "kontrol": entry["specs"].get("kontrol"),
                    "kanaler": entry["specs"].get("kanaler"),       
                }
            else:
                specs = {}

            # Create product using ProductCreate schema
            product = ProductCreate(
                id=entry.get("id", ""),
                productname=entry.get("productname", ""),
                kategori=entry.get("kategori", ""),
                producent=entry.get("producent", ""),
                color=entry.get("color", ""),
                pris=entry.get("pris", 0),
                stock=entry.get("stock", 0),
                desc=entry.get("desc", ""),
                image=f"/static/{entry['kategori'].lower().replace(' ', '_')}/{entry['image']}",
                specs=specs
            )
            
            create_product(db, product)

    except Exception as e:
        print(f"Error loading data: {str(e)}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    load_data()