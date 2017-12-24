from flask import Flask, render_template
from flask_socketio import SocketIO,send,emit
from pymongo import MongoClient
from threading import Thread
from time import sleep
import logging
import logging.handlers
import sys
logger = logging.getLogger('logging')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler(sys.stdout)
logger.addHandler(ch)
logger.debug("hello")
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret' # TODO: put it to config
socketio = SocketIO(app)
client = MongoClient("mongodb://localhost:27017")


@socketio.on('hello')
def handle_hello(message):
    logger.debug("on hello",message)
    send(message)

@socketio.on('message')
def handle_message(message):
    logger.debug("on message")
    emit("hello",message)

@socketio.on('connect')
def handle_connect():
    logger.debug("client connected")
@socketio.on('json')
def handle_json(json):
    print('received json: ' + str(json))

if __name__ == '__main__':
    socketio.run(app,'0.0.0.0')
