from .database import base
from sqlalchemy import Column,INTEGER,String
class Employee(base):
    __tablename__ ="employees"
    id=Column(INTEGER,primary_key=True,index=True)
    name = Column(String)
    address = Column(String)
    mobileNumber =Column(INTEGER) 
