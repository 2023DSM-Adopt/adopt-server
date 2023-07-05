from fastapi import FastAPI


def include_admin_router(app: FastAPI):
    from admin.view import admin_router

    app.include_router(admin_router)