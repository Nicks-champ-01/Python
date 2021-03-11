from pydantic import BaseModel
class Employee(BaseModel):
  name:str
  address:str
  mobileNumber:int
