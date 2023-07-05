from fastapi import APIRouter

from main import session_scope, Application
from user.payload import CreateApplicationRequest

user_router = APIRouter()


@user_router.post('/application')
def application_adopt(animal_id: int, request: CreateApplicationRequest):  # 입양 등록
    with session_scope() as session:
        session.add(
            Application(
                animal_id=animal_id,
                **request.dict()
            )
        )


@user_router.get('/adopt/list')  # 입양 등록 리스트
def get_adopt_list():
    pass