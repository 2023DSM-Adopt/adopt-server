from fastapi import FastAPI


def include_image_router(app: FastAPI):
    from images.view import image_router

    app.include_router(image_router)
