from fastapi.logger import logger
from sqlalchemy.orm import Session
from src.database_models import Notification
from src.schemas import NotificationCreate


def get_notifications(db: Session, offset: int = 0, limit: int = 100):
    return db.query(Notification).offset(offset).limit(limit).all()


def create_notification(db: Session, notification: NotificationCreate):
    db_notification = Notification(**notification.dict())
    db.add(db_notification)
    db.commit()
    db.refresh(db_notification)
    return db_notification


def create_notifications_bulk(db: Session, notifications: list[NotificationCreate]):
    """Create notification entries and send notifications.

    :param db: sqlalchemy db object
    :param notifications: list of notification items
    :return: None
    """
    # Here we could be sending mobile push notifications, email notifications or notify users
    # using other communication channels (here we just mock/log this action, not implemented)
    logger.info("Sending notifications")

    # Create database entries, so that e.g. users can list their notifications
    # within their mobile or web application.
    for notification in notifications:
        db_notification = Notification(**notification.dict())
        db.add(db_notification)

    db.commit()
