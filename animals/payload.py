from datetime import date
from typing import Optional

from pydantic import BaseModel


class CreateAnimalRequest(BaseModel):
    weight: float
    breeds: str
    animal_kind: str
    is_neutered: bool
    hair_color: str
    found_at: str
    found_age: str
    found_date: date
    image_url: str
    town: str
    introduce: str
    status: Optional[str]