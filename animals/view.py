from fastapi import APIRouter

from animals.payload import CreateAnimalRequest
from main import session_scope, Animal

animal_router = APIRouter()


@animal_router.post('/animals')
def register_animal(request: CreateAnimalRequest):  # 동물 등록
    animal = Animal(**request.dict())

    with session_scope() as session:
        session.add(animal)

    return {
        'animal_id': animal.id_
    }


@animal_router.get('/animals/detail')
def get_animal_detail(animal_id: int):
    with session_scope() as session:
        animal = session.query(Animal).filter(Animal.id_ == animal_id).one()

        return {
            'id': animal.id_,
            'sex': animal.sex,
            'weight': animal.weight,
            'breeds': animal.breeds,
            'animal_kind': animal.animal_kind,
            'is_neutered': animal.is_neutered,
            'hair_color': animal.hair_color,
            'found_at': animal.found_at,
            'found_age': animal.found_age,
            'found_date': animal.found_date,
            'image_url': animal.image_url,
            'town': animal.town,
            'introduce': animal.introduce,
            'status': animal.status
        }


@animal_router.get('/animals/non-detail')
def get_animal_detail(animal_id: int):
    with session_scope() as session:
        animal = session.query(Animal).filter(Animal.id_ == animal_id).one()

        return {
            'id': animal.id_,
            'breeds': animal.breeds,
            'sex': animal.sex,
            'image_url': animal.image_url,
            'town': animal.town,
            'status': animal.status
        }
