from typing import Union
from pydantic import BaseModel


class NotificationBase(BaseModel):
    title: str
    text: Union[str, None] = None


class NotificationCreate(NotificationBase):
    pass


class Notification(NotificationBase):
    class Config:
        orm_mode = True
