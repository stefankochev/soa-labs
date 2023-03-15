from sqlalchemy.orm import Session
from src.database_models import Notification
from src.schemas import NotificationCreate


def get_notifications(db: Session, offset: int = 0, limit: int = 100):
    return db.query(Notification).offset(offset).limit(limit).all()


def create_notification(db: Session, item: NotificationCreate):
    db_notification = Notification(**item.dict())
    db.add(db_notification)
    db.commit()
    db.refresh(db_notification)
    return db_notification
