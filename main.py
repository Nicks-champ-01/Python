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
d = datetime.datetime.now()
year =str(d.year)
month= str(d.month)
day = str(d.day)
hour = str(d.hour)
min = str(d.minute)
second =str(d.second)
mdy= (month+" - "+ day + " - " + year)
t = (hour+" : " + min + " : " + second)
@app.get('/')
def index():
  return {
    "Current-Date ": mdy,
    "Current-Time": t
  }
# @app.get('/employee')
# def get_employee():
#   return db
# @app.get('/employee/{employee_id}')
# def get_employeeId(employee_id:int):
#   return db[employee_id-1]
# @app.post('/employee')
# def create_employee(employee:Employee):
#   db.append(employee.dict())
#   return db[-1]
# @app.delete('/employee/{employee_id}')
# def delete_employee(employee_id:int):
#   db.pop(employee_id-1)
#   return {}

