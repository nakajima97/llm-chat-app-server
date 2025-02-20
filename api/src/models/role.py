from sqlalchemy import Column, BigInteger, Text
from src.databases.db import Base


class Role(Base):
    __tablename__ = "roles"

    id = Column(BigInteger, primary_key=True)
    name = Column(Text, nullable=False)
