from app.models import Address, Pet, Session, Base, User, engine


def create_tables():
    Base.metadata.create_all(engine)


def populate_tables(session: Session):
    users = [User(id=i, name=f'user {i}', fullname=f'fullname {i}', nickname=f'#{i}') for i in range(1, 11)]
    pets = [Pet(id=i, name=f'pet {i}', age=i, pet_type=f'type {i}') for i in range(1, 11)]
    addresses = [Address(id=i, email=f'email{i}@gmail.com', user_id=i) for i in range(1, 11)]
    session.add_all(users)
    session.add_all(pets)
    session.add_all(addresses)
    session.commit()

    # create assocs
    for number, pet in enumerate(pets):
        pet.users = [users[number]]
    
    session.commit()


def setup_db() -> Session:
    session = Session()

    # drop all tables
    Base.metadata.drop_all(engine)

    # create and populate tables
    create_tables()
    populate_tables(session)


if __name__ == '__main__':
    setup_db()
