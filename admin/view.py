from fastapi import APIRouter, HTTPException

from main import Animal, session_scope, Post, Adopt
from admin.payload import CreatePostRequest, CreateAdoptRequest

admin_router = APIRouter()


@admin_router.post('/animals/post')
def create_animal_post(animal_id: int, request: CreatePostRequest):  # 공고 작성
    post = Post(
        animal_id=animal_id,
        **request.dict()
    )

    with session_scope() as session:
        session.add(post)


@admin_router.post('/animals/adopt')
def create_animal_adopt(animal_id: int, request: CreateAdoptRequest):  # 입양 게시물 작성
    adopt = Adopt(
        animal_id=animal_id,
        **request.dict()
    )

    with session_scope() as session:
        animal = session.query(Animal).filter(Animal.id_ == animal_id).one()

        if animal.status == '공고중':
            raise HTTPException(
                status_code=400,
                detail='공고중에는 입양할 수 없습니다'
            )

        session.add(adopt)
