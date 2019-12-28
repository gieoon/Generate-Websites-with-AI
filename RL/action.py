# Each action is either addition or deletion + a DOM element type + a CSS name
# These are modified directly into the HTML
# This is encoded as a step into the NN

import numpy as np


vocab = []
with open('./vocab.txt', 'r') as f:
    for line in f:
        vocab.append(line.strip())

print("vocab: ", vocab)

actions = [
    'INSERT',
    'DELETE'
]

vocab_weights = [0 for _ in range(len(vocab))]
action_weights = [0 for _ in range(len(actions))]
#out = open('./out.GENERATED', 'w') # 'a' = append mode
blankFile = open('./blank.html', 'r')
out = []
history = []
# How to make the weights go through 
# What kind of input is the target? 
# What kind of input is being adjusted for?
# How does the algorithm read data, is it using a LSTM?

def generateHTMLAction(target):
    #print("generating action: ", target)
    v = vocab[np.random.randint(0, len(vocab))]
    #print(v)
    a = selectAction() #TODO take in parameter of the whole file to see where the action should be inserted
    l = selectLocation(v, a)
    performAction(v, a, l)

    # Increment the average of that action
    # Edit the file
    # Track the action so we know what was done, and understand that action
    # Use a LSTM to process the data

def selectAction():
    a = np.random.randint(0, 2)
    #print(actions[a])
    return 0
    #TODO return a

# Generate the location in the file to generate the action at
# This is dependent on the type of action that we want to perform
def selectLocation(v, actionType):
    #print("")
    return 0

# When a human selects an action, then increase the importance of all of the weights that the human selected, then continue

# Perform an action using vocab, an action, and a location to perform it at
def performAction(v, a, l):
    print("performing action")
    #out.write("<{}>Generated {}</{}>\n".format(v, v, v))
    out.append("<{}>Generated {}</{}>\n".format(v, v, v))
    history.append("{}-{}-{}".format(v,a,l))


def displayHTMLFile():
    html = blankFile.readlines()
    print("out: ", html)
    #contents = out.readlines()
    html.insert(7, ''.join(out))
    print(html)
    del out[:]
    return html
    #out[:] = []
        