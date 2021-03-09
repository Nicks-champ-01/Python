# Python
you have to setup the virtual enviroment
python3 -m venv tutorial-env
then afterwords you to activate it
for mac-os  source tutorial-env/bin/activate
for windows you have to go the directory and in it scripts then u have to write activate.bat
as after this commands your virtual enviroment would be activated 
you have to see what things  you have got in your pip list by command pip list
if you dont have fastapi hypercorn or uvicorn then you need to install it by using 
pip3 install fastapi
pip3 install hypercorn
or
pip3 install  uvicorn
for running the code in hyoercorn u have to write  hypercorn  your fileName:app --reload
for running the code in uvicorn u have to write  uvicorn  your fileName:app --reload
