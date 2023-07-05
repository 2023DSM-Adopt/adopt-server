from os import getcwd

from fastapi import APIRouter, UploadFile
from starlette.responses import FileResponse

from images.payload import UploadImageResponse

image_router = APIRouter(tags=['images'])


@image_router.post('/images')
def upload_images(file: UploadFile):
    file_name = file.filename

    with open(getcwd() + '/' + file_name, 'wb') as buffer:
        buffer.write(file.file.read())

    return UploadImageResponse(
        file_name=file_name
    )


@image_router.get('/images/{file_name}')
def find_file(file_name: str):
    image = getcwd() + '/' + file_name

    return FileResponse(image, media_type='image/jpeg')
