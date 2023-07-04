# config.py
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

MYSQL_URL = os.environ['MYSQL_URL']

# rdbms.py
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.sql import false
from sqlalchemy import create_engine, DATE, DATETIME, FLOAT, BOOLEAN

engine = create_engine(
    url=MYSQL_URL,
    pool_recycle=3600,
    pool_size=20,
    max_overflow=20,
    pool_pre_ping=True
)
session = sessionmaker(bind=engine, autocommit=False, autoflush=False, expire_on_commit=False)

# models.py
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, CHAR, VARCHAR, INTEGER, ForeignKey

Base = declarative_base()


class User(Base):
    __tablename__ = 'tbl_user'
    id_ = Column('id', INTEGER, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(5), nullable=False)
    phone_num = Column(CHAR(11), nullable=False, unique=True)


class Application(Base):
    __tablename__ = 'tbl_application'
    user_id = Column(INTEGER, ForeignKey('tbl_user.id'), primary_key=True)
    animal_id = Column(INTEGER, ForeignKey('tbl_animal.id'), primary_key=True)
    title = Column(VARCHAR(255), nullable=False)
    content = Column(VARCHAR(255), nullable=False)
    meet_at = Column(DATETIME, nullable=False)


class Animal(Base):
    __tablename__ = 'tbl_animal'
    id_ = Column('id', INTEGER, primary_key=True, autoincrement=True)

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

    status = Column(VARCHAR(10), nullable=False)


class Post(Base):
    __tablename__ = 'tbl_post'
    animal_id = Column(INTEGER, ForeignKey('tbl_animal.id'), primary_key=True)
    post_id = Column(INTEGER, primary_key=True, autoincrement=True)

    start_at = Column(DATE, nullable=False)
    end_At = Column(DATE, nullable=False)


class Adopt(Base):
    __tablename__ = 'tbl_adopt'
    animal_id = Column(INTEGER, ForeignKey('tbl_animal.id'), primary_key=True)
    start_at = Column(DATE, nullable=False)


Base.metadata.create_all(engine)

# cqrs.py


# service.py


# view.py


from fastapi import FastAPI

app = FastAPI()

if __name__ == '__main__':
    from uvicorn import run
    from starlette.middleware.cors import CORSMiddleware

    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    run(app)
