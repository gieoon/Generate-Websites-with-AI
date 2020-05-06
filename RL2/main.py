# Implement q-learning.
import numpy as np
from flask import Flask, render_template
from flask_socketio import SocketIO

from action import generateHTMLAction, displayHTMLFile

app = Flask(__name__)
socketio = SocketIO(app)

k = 5

# Number of steps before human intervention
ACTION_STEPS = 10

@app.route('/')
def run():
    count = 0
    target = 1# np.array() # What input is to be used here?

    while True and count < ACTION_STEPS:
        count += 1
        
        step(target)

        if count % ACTION_STEPS == 0:
            # Generate and send to discriminator
    #print("target: ", ''.join(target))
    return ''.join(target)

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)

@socketio.on('json')
def handle_json(json):
    print('received json: ' + str(json))

if __name__ == '__main__':
    socketio.run(app)
