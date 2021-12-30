from fastapi import FastAPI
from db_setup import setup_db
from models import Session, User

app = FastAPI()


@app.on_event('startup')
def setup_database():
    setup_db()


@app.get('/users')
def get_all_users():
    session = Session()
    return session.query(User).all()


@app.get('/users/{user_id}')
def get_user(user_id: int):
    session = Session()
    return session.query(User).filter(User.id==user_id).one()
