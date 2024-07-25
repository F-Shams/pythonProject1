from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


Base = declarative_base()
db_url = 'sqlite:///db.sqlite'
engine = create_engine(db_url)


class Animal(Base):
    __tablename__ = 'table1'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    color = Column(String)


Base.metadata.create_all(engine)

animal0 = Animal(name='dog', color='brown')
animal1 = Animal(name='cat', color='white')
animal2 = Animal(name='donkey', color='black')


Session = sessionmaker(bind=engine)
session = Session
session.add(animal0)
session.add_all([animal1, animal2])

to print animals
animals = session.



