import os
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.param_functions import Query
from db_setup import setup_db
from models import User, Pet
from dependencies import get_session
from request_models import GetUsersParams, UpdateUserParams

app = FastAPI()


@app.on_event('startup')
def setup_database():
    if not os.path.exists('my_db.db'):
        setup_db()


@app.get('/users')
def get_users(params: GetUsersParams = Depends(), session=Depends(get_session)):
    """
    Filters users by provided params. None is ignored.
    """
    query = session.query(User)
    for k, v in params.dict().items():
        if v is not None:
            query = query.filter(getattr(User, k)==v)
    
    return query.all()


@app.put('/users')
def update_user(params: UpdateUserParams,
                session=Depends(get_session)):
    user = session.query(User).filter(User.id==params.id).first()
    if user is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"User with id={params.id} doesn't exist.")

    user.name = params.name
    user.fullname = params.fullname
    user.nickname = params.nickname
    session.commit()
    return 200


@app.get('/pets')
def get_all_pets(session=Depends(get_session)):
    return session.query(Pet).all()


@app.get('/pets/{pet_id}')
def get_pet(pet_id: int, session=Depends(get_session)):
    return session.query(Pet).filter(Pet.id==pet_id).all()
