# The reinforcement learning loop

import numpy as np
from action import generateHTMLAction, displayHTMLFile

from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

k = 5

# Number of steps before human intervention
HUMAN_INTERVENTION = 10

# Action values
Q = [0 for _ in range(k)]

# The number of times each action was taken
N = [0 for _ in range(k)]

# Epsilon value for exploration
eps = 0.1

# Perform step to generate HTML
def step(target):
    generateHTMLAction(target)

def humanIntervention():
    #print("human intervention")
    # Human chooses either the image on the left or the image on the right
    return displayHTMLFile()
    #TODO return 1 # 0 or 1

@app.route('/')
def helloWorld():
    count = 0
    target = 1# np.array() # What input is to be used here?

    while True and count < HUMAN_INTERVENTION:
        count += 1
        
        step(target)

        if count % HUMAN_INTERVENTION == 0:
            target = humanIntervention()
    print("target: ", ''.join(target))
    return ''.join(target)

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)

@socketio.on('json')
def handle_json(json):
    print('received json: ' + str(json))

if __name__ == '__main__':
    socketio.run(app)
