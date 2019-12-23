# The reinforcement learning loop

import numpy as np
from action import generateHTMLAction

k = 5

# Number of steps before human intervention
h = 5

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
    return 1 # 0 or 1

count = 0
target = 1# np.array() # What input is to be used here?

while True:
    count += 1
    
    step(target)

    if count % h == 0:
        target = humanIntervention()