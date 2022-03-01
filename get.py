from pydantic import BaseModel
from models import Session, Base


def get(table: Base, model: BaseModel, session: Session):
    query = session.query(table)
    for k, v in model.dict().items():
        if v is not None:
            query = query.filter(getattr(table, k)==v)
    
    return query.all()
