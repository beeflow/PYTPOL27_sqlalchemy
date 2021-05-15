"""copyright (c) 2021 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    email = Column(String(100))
    phone = Column(String(12), nullable=True)
    card_number = Column(String(9))

    first_name_id = Column(Integer, ForeignKey("first_name.id"))
    first_name = relationship("FirstName", back_populates="users")

    last_name_id = Column(Integer, ForeignKey("last_name.id"))
    last_name = relationship("LastName", back_populates="users")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"