# Each action is either addition or deletion + a DOM element type + a CSS name
# These are modified directly into the HTML
# This is encoded as a step into the NN

import numpy as np

vocab = []
with open('./vocab.txt', 'r') as f:
    for line in f:
        vocab.append(line.strip())

print("vocab: ", vocab)

weights = [0 for _ in range(len(vocab))]
out = open('./out.GENERATED', 'w')

def generateHTMLAction(target):
    #print("generating action: ", target)
    r = vocab[np.random.randint(0, len(vocab))]
    a = selectAction()
    print(selectAction())

    # Increment the average of that action...how to do this?

def selectAction():
    return np.random.randint(0, 2)