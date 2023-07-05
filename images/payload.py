from pydantic import BaseModel


class UploadImageResponse(BaseModel):
    file_name: str