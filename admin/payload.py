from datetime import date

from pydantic import BaseModel


class CreatePostRequest(BaseModel):
    start_at: date
    end_at: date


class CreateAdoptRequest(BaseModel):
    start_at: date
