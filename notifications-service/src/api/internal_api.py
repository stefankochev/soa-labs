from fastapi import APIRouter, Depends
from fastapi.logger import logger

from sqlalchemy.orm import Session

from src.database import get_db
from src import schemas
from src import crud


router = APIRouter(prefix="/internal", tags=["internal"])


@router.post("/notifications/send", response_model=dict)
def send_notifications_bulk(
    notifications: list[schemas.NotificationCreate], db: Session = Depends(get_db)
):
    """Bulk send notifications."""
    crud.create_notifications_bulk(db=db, notifications=notifications)
    return {"status": "ok"}


@router.post("/notifications/scheduled", response_model=dict)
def send_scheduled_notifications(db: Session = Depends(get_db)):
    """Bulk send scheduled notifications CRON task."""
    # The endpoint is executed every 15 minutes:
    # 1. Fetch scheduled, unsent notifications in the database,
    #    i.e. notifications not immediately sent, but scheduled to be sent later
    # 2. Sent the scheduled notifications and mark the entries as "sent"
    # 3. Return response
    # Not Implemented, mock
    logger.info("Sending scheduled notifications...")
    return {"status": "ok"}
