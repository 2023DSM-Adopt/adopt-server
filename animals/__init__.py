from fastapi import FastAPI


def include_animal_router(app: FastAPI):
    from animals.view import animal_router

    app.include_router(animal_router)
