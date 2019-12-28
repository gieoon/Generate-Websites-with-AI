# Each action is either addition or deletion + a DOM element type + a CSS name
# These are modified directly into the HTML
# This is encoded as a step into the NN

import numpy as np


vocab = []
with open('./vocab.txt', 'r') as f:
    for line in f:
        vocab.append(line.strip())
cssVocab = [] 
with open('./css_vocab.txt','r') as f:
    for line in f:
        cssVocab.append(line.strip())

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
    css = createCSSForAction(v)
    #print("css 2: ", css)
    performAction(v, css, a, l)

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
def performAction(v, css, a, l):
    #print("performing action")
    #out.write("<{}>Generated {}</{}>\n".format(v, v, v))
    out.append("<{} {}>Generated {}</{}>".format(v, css, v, v))
    history.append("{}_{}_{}_{}".format(v,css,a,l))

# Generates inline css to be used
def createCSSForAction(v):
    # generate based on history
    noOfStyles = np.random.randint(0, len(cssVocab))
    res = ''
    for i in range(noOfStyles):
        s = cssVocab[np.random.randint(0, len(cssVocab))]
        value = getCSSValue(s)
        res += "{}:{};".format(s, value)
    
    #print("creating css 1: ", res)
    return 'style="{}"'.format(res)

def getCSSValue(s):
    if s == 'color' or s == 'background-color':
        return ['blue','green','yellow','red'][np.random.randint(0, 3)]
    elif s == 'width':
        return str(np.random.randint(1, 100)) + 'vw'
    elif s == 'height':
        return str(np.random.randint(1, 100)) + 'vh'
    elif s == 'display':
        return ['flex','inline-block','block'][np.random.randint(0, 3)]
    elif s == 'position':
        return ['absolute','relative','fixed'][np.random.randint(0, 3)]

def displayHTMLFile():
    html = blankFile.readlines()
    #print("out: ", html)
    #contents = out.readlines()
    html.insert(7, ''.join(out))
    print(html)
    del out[:]
    #out = []
    return html
    #out[:] = []
        