import os
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.param_functions import Path
from db_setup import setup_db
from models import User, Pet
from dependencies import get_session
from request_models import GetUserParams, UpdateUserParams, InsertUserParams
from request_models import GetPetParams

app = FastAPI()


@app.on_event('startup')
def setup_database():
    if not os.path.exists('my_db.db'):
        setup_db()


@app.get('/users')
def get_users(params: GetUserParams = Depends(),
              session=Depends(get_session)):
    """
    Filters users by provided params. None is ignored.
    """
    query = session.query(User)
    for k, v in params.dict().items():
        if v is not None:
            query = query.filter(getattr(User, k)==v)
    
    return query.all()


@app.put('/users/update')
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


@app.delete('/users/{id}/delete')
def delete_user(id: int = Path(...),
                session=Depends(get_session)):
    user_to_delete = session.query(User).filter(User.id==id).first()
    if user_to_delete:
        session.delete(user_to_delete)
        session.commit()

    return 200
    

@app.put('/users/new')
def new_user(params: InsertUserParams,
             session=Depends(get_session)):
    user = session.query(User).filter(User.id==params.id).first()
    if user:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail=f'User with id={params.id} already exists.')
    
    user = User(**params.dict())
    session.add(user)
    session.commit()
    return 200


@app.get('/pets')
def get_all_pets(params: GetPetParams = Depends(),
                 session=Depends(get_session)):
    pet = session.query(Pet)
    for k, v in params.dict().items():
        if v is not None:
            pet = pet.filter(getattr(Pet, k)==v)
    
    return pet.all()
