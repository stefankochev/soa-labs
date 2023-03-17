import requests
from fastapi.logger import logger
from sqlalchemy.orm import Session
from src.database_models import Item
from src.requests_common import notifications_service_request
from src.schemas import ItemCreate
from src.settings import NOTIFICATIONS_SERVICE_URL


def get_items(db: Session, offset: int = 0, limit: int = 100):
    return db.query(Item).offset(offset).limit(limit).all()


def create_item(db: Session, item: ItemCreate):
    db_item = Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    try:
        notifications = [
            {"title": f"Title {i}", "text": f"Text {i}"} for i in range(5)
        ]
        notifications_service_request(
            "POST",
            url=f"{NOTIFICATIONS_SERVICE_URL}/internal/notifications",
            json=notifications,
        )
    except Exception as ex:
        logger.exception(ex)

    return db_item
