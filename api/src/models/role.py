from sqlalchemy import Column, BigInteger, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Role(Base):
    __tablename__ = 'roles'
    
    id = Column(BigInteger, primary_key=True)
    name = Column(Text, nullable=False)
