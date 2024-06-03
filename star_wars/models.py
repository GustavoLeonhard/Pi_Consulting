from database import Base
from sqlalchemy import Column, Integer, String, Float


class Character(Base):
    __tablename__: str = 'character'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    height = Column(Float)
    mass = Column(Float)
    hair_color = Column(String)
    skin_color = Column(String)
    eye_color = Column(String)
    birth_year = Column(Integer)
