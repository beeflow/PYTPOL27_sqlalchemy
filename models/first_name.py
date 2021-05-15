"""copyright (c) 2021 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class FirstName(Base):
    __tablename__ = "first_name"

    id = Column(Integer, primary_key=True)
    name = Column(String(15), name="first_name")

    def __str__(self):
        return self.name
