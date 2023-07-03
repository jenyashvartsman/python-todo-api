from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Boolean

from database import engine

Base = declarative_base()

class Todo(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True)
    todo = Column(String)
    completed = Column(Boolean, default=False)

Base.metadata.create_all(engine)