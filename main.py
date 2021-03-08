from fastapi import  FastAPI
import uvicorn
import datetime
# import pytz  # for timezone
app =FastAPI()
d = datetime.datetime.now()
year =str(d.year)
month= str(d.month)
day = str(d.day)
hour = str(d.hour)
min = str(d.minute)
second =str(d.second)
yzw = (month+" - "+ day + " - " + year)
t = (hour+" : " + min + " : " + second)
@app.get('/')
def index():
  return {
    "Current-Date ": yzw,
    "Current-Time": t

  }