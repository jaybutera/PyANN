from graph import *
import matplotlib.pyplot as plt
from random import random

# Evenutally merge these two update weight functions to work with both output
# and hidden nodes.
def updateOutputWeight(node, lower, targ, alpha):
    node.setWeight(lower, node.getWeight(lower) + alpha * node.activate() * node.getChange(targ))

def updateHiddenWeight(node, lower, di, alpha):
    node.setDi(di)
    node.setWeight(lower, node.getWeight(lower) + alpha * node.activate() * node.getChange())

def backProp_test():
    """
    Tests the back propagation algorithm with an arbitrary data set
    """

    # Interestingly, the NN convergers when the value is under 1. However,
    # occasionaly it will diverge and appproach positive or negative infinity.

    g = Graph()
    outputs = []
    target = .2
    alpha = .01
    MAX = 1000

    inputs = [g.addNode(i, kin='input', ix = float(i+1)) for i in range(3)]
    hidden = [g.addNode(i) for i in range(3,5)]
    output = g.addNode(5, kin='output')

    # To hidden
    g.addEdge(3,0,weight=round(random(),2))
    g.addEdge(4,0,weight=round(random(),2))
    g.addEdge(4,1,weight=round(random(),2))
    g.addEdge(4,2,weight=round(random(),2))
    g.addEdge(3,1,weight=round(random(),2))
    g.addEdge(3,2,weight=round(random(),2))

    # To output
    g.addEdge(5,3,weight=round(random(),2))
    g.addEdge(5,4,weight=round(random(),2))

    # I hope you're ashamed of yourself. Shun yourself for the ugly code that
    # is below this comment
    di = [0 for i in range(len(hidden))]

    for i in range(MAX):
        for idx, outputWeight in enumerate(output.getConnections()):
            di[idx] = output.getChange(target)
            updateOutputWeight(output, outputWeight, target, alpha)

        for idx, hiddenNode in enumerate(hidden):
            for inputWeight in hiddenNode.getConnections():
                updateHiddenWeight(hiddenNode, inputWeight, di[idx], alpha)

        print 'output:', output.activate()
        outputs.append(output.activate())

    # Plot information
    plt.figure(1)
    plt.clf()
    plt.title('ANN Output Value Evolution')
    plt.ylabel('Output value')
    plt.xlabel('Epoch')
    plt.ylim(0,10)

    # Plot the output node at each epoch
    plt.plot(range(MAX), outputs, 'b-')
    # Plot the target value line (trend should converge here)
    plt.axhline(target, color='r')

    plt.show()
