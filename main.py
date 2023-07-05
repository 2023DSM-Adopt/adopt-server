# config.py
import os
from uuid import uuid4
from fastapi import HTTPException

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

MYSQL_URL = os.environ['MYSQL_URL']

# rdbms.py
from sys import exc_info
from contextlib import contextmanager

from sqlalchemy.sql import false
from sqlalchemy.orm import sessionmaker, scoped_session, Session
from sqlalchemy import create_engine, DATE, DATETIME, FLOAT, BOOLEAN, func

engine = create_engine(
    url=MYSQL_URL,
    pool_recycle=3600,
    pool_size=20,
    max_overflow=20,
    pool_pre_ping=True
)
session = scoped_session(
    sessionmaker(
        bind=engine,
        autocommit=False,
        autoflush=False,
        expire_on_commit=False
    )
)


@contextmanager
def session_scope() -> Session:
    try:
        yield session
        session.commit()

    except:
        session.rollback()
        typ, cls, traceback = exc_info()

        raise HTTPException(
            status_code=500,
            detail={
                'exception': str(typ.__name__),
                'explain': str(cls),
            }
        )


# models.py
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, CHAR, VARCHAR, INTEGER, ForeignKey

Base = declarative_base()


class Application(Base):
    __tablename__ = 'tbl_application'

    user_name = Column(VARCHAR(5), nullable=False)
    user_phone_num = Column(CHAR(11), nullable=False, primary_key=True)
    animal_id = Column(INTEGER, ForeignKey('tbl_animal.id'), primary_key=True)
    title = Column(VARCHAR(255), nullable=False)
    content = Column(VARCHAR(255), nullable=False)
    meet_at = Column(DATETIME, nullable=False)
    create_at = Column(DATE, nullable=False)


class Animal(Base):
    __tablename__ = 'tbl_animal'
    id_ = Column('id', INTEGER, primary_key=True, autoincrement=True)

    sex = Column(CHAR(1), nullable=False)
    weight = Column(FLOAT, nullable=False)
    breeds = Column(VARCHAR(255), nullable=False)
    animal_kind = Column(VARCHAR(255), nullable=False)
    is_neutered = Column(BOOLEAN, nullable=False, server_default=false())
    hair_color = Column(VARCHAR(255), nullable=False)

    found_at = Column(VARCHAR(255), nullable=False)
    found_age = Column(INTEGER, nullable=False)
    found_date = Column(DATE, nullable=False)

    image_url = Column(VARCHAR(255), nullable=False)
    town = Column(VARCHAR(255), nullable=False)
    introduce = Column(VARCHAR(255), nullable=False)

    status = Column(VARCHAR(10), nullable=False, default='대기중', server_default='대기중')


class Post(Base):
    __tablename__ = 'tbl_post'
    animal_id = Column(INTEGER, ForeignKey('tbl_animal.id'), primary_key=True)
    post_id = Column(CHAR(36), autoincrement=True, nullable=False, default=uuid4)

    start_at = Column(DATE, nullable=False)
    end_at = Column(DATE, nullable=False)


class Adopt(Base):
    __tablename__ = 'tbl_adopt'
    animal_id = Column(INTEGER, ForeignKey('tbl_animal.id'), primary_key=True)
    start_at = Column(DATE, nullable=False)



# settings.py
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from user import include_user_router
from admin import include_admin_router
from images import include_image_router
from animals import include_animal_router

app = FastAPI()

include_user_router(app)
include_admin_router(app)
include_animal_router(app)
include_image_router(app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
