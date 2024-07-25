from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


Base = declarative_base()
db_url = 'sqlite:///db.sqlite'
engine = create_engine(db_url)


class Animals(Base):
    __tablename__ = 'table1'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    color = Column(String)


Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session
session.commit()


