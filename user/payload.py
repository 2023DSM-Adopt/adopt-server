from datetime import date, datetime

from pydantic import BaseModel


class CreateApplicationRequest(BaseModel):
    user_name: str
    user_phone_num: str
    user_id: str
    title: str
    content: str
    meet_at: datetime
    create_at: date
