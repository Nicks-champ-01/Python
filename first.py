from fastapi import  FastAPI
import uvicorn
import datetime
from pydantic import BaseModel
# import pytz  # for timezone
app =FastAPI()
db = []
class Employee(BaseModel):
  name:str
  address:str
  mobileNumber:int
@app.get('/employee')
def get_employee():
  return db
@app.get('/employee/{employee_id}')
def get_employeeId(employee_id:int):
  return db[employee_id]
@app.post('/employee')
def create_employee(employee:Employee):
  db.append(employee.dict())
  return db[-1]
@app.delete('/employee/{employee_id}')
def delete_employee(employee_id:int):
  db.pop(employee_id-1)
  return {employee_id}

