from fastapi import FastAPI


def include_user_router(app: FastAPI):
    from user.view import user_router

    app.include_router(user_router)
