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
session = Session()

session.add(animal0)
session.add_all([animal1, animal2])

animals = session.query(Animal).all()
for animal in animals:
    print(animal.name, animal.color)


filtered_animals = session.query(Animal).filter_by(color='black')
for animal in filtered_animals:
    print(f"{animal.name} and {animal.color}")

to_filter2 = session.query(Animal).filter_by(name='dog')
print(to_filter2)




