"""copyright (c) 2021 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class LastName(Base):
    __tablename__ = "last_name"

    id = Column(Integer, primary_key=True)
    name = Column(String(15), name="last_name")

    def __str__(self):
        return self.name
