arg backend
from mongo

run apt -qq update && apt install -qq -y python3-pip
run pip3 install flask pymongo eventlet flask-socketio

expose 27017 5000
workdir /app
# copy ./backend /app
cmd mongod --fork --logpath /var/log/mongod.log && python3 main.py
