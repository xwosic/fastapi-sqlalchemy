from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.sql.schema import ForeignKey


engine = create_engine('sqlite:///my_db.db', echo=True, connect_args={"check_same_thread": False})

Base = declarative_base()

Session = sessionmaker(bind=engine)


class Pet(Base):  # type: ignore
    __tablename__ = 'pets'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    pet_type = Column(String)

    # many to many
    users = relationship('User', secondary='users_pets', back_populates='pets')

    def __repr__(self):
        return f'Pet(id={self.id}, name={self.name}, age={self.age}, pet_type={self.pet_type})'


class User(Base):  # type: ignore
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    # one to many
    addresses = relationship('Address', back_populates='user', cascade='all, delete, delete-orphan')

    # many to many
    pets = relationship('Pet', secondary='users_pets', back_populates='users')

    def __repr__(self):
        return f'User(id={self.id}, name={self.name}, fullname={self.fullname}, nickname={self.nickname})'


class UserPet(Base):  # type: ignore
    __tablename__ = 'users_pets'
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    pet_id = Column(Integer, ForeignKey('pets.id'), primary_key=True)


class Address(Base):  # type: ignore
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)

    # many to one
    # in foreignkey's constructor we specify column name of table to which it is related
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates='addresses')

    def __repr__(self):
        return f"Address(id={self.id}, email={self.email})"


if __name__ == '__main__':
    # we don't want to accidently overwrite db
    Base.metadata.create_all(engine)