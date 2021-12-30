from fastapi import FastAPI, Depends
from db_setup import setup_db
from models import User, Pet
from dependencies import get_session

app = FastAPI()


@app.on_event('startup')
def setup_database():
    setup_db()


@app.get('/users')
def get_all_users(session=Depends(get_session)):
    return session.query(User).all()


@app.get('/users/{user_id}')
def get_user(user_id: int, session=Depends(get_session)):
    return session.query(User).filter(User.id==user_id).all()


@app.get('/pets')
def get_all_pets(session=Depends(get_session)):
    return session.query(Pet).all()


@app.get('/pets/{pet_id}')
def get_pet(pet_id: int, session=Depends(get_session)):
    return session.query(Pet).filter(Pet.id==pet_id).all()
