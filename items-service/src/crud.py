import json
from sqlalchemy.orm import Session

from src.database_models import Item
from src.pubsub.producer import get_producer
from src.schemas import ItemCreate
from src.settings import ITEMS_TOPIC
from starlette.concurrency import run_in_threadpool


def get_items(db: Session, offset: int = 0, limit: int = 100):
    return db.query(Item).offset(offset).limit(limit).all()


async def create_item(db: Session, item: ItemCreate):
    db_item = Item(**item.dict())
    db.add(db_item)

    await run_in_threadpool(db.commit)
    await run_in_threadpool(db.refresh, db_item)

    await get_producer().send(
        ITEMS_TOPIC,
        json.dumps(
            {
                "id": db_item.id,
                "title": db_item.title,
                "description": db_item.description,
            }
        ).encode("ascii"),
    )

    return db_item
