from sqlalchemy.orm import Session
from src.database_models import Item
from src.schemas import ItemCreate


def get_items(db: Session, offset: int = 0, limit: int = 100):
    return db.query(Item).offset(offset).limit(limit).all()


def create_item(db: Session, item: ItemCreate):
    db_item = Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
