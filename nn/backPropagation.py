import json
from graph import *
import matplotlib.pyplot as plt
from random import random

# Evenutally merge these two update weight functions to work with both output
# and hidden nodes.
def updateOutputWeight(node, lower, targ, alpha):
    node.set_weight(lower, node.getWeight(lower) + alpha * node.activate() * node.get_change(targ))

def updateHiddenWeight(node, lower, di, alpha):
    node.setDi(di)
    node.set_weight(lower, node.getWeight(lower) + alpha * node.activate() * node.get_change())

"""
def run(filepath):
    ""
    Runs a specified network via JSON with
    a specified number of epochs.
    ""
    g = Graph()

    for i in range(MAX):
        for ind in target:
            for idx, outputWeight in enumerate(output.getConnections()):
                di[idx] = output.get_change(ind[1])
                updateOutputWeight(output, outputWeight, ind[1], alpha)

            for idx, hiddenNode in enumerate(hidden):
                for inputWeight in hiddenNode.getConnections():
                    updateHiddenWeight(hiddenNode, inputWeight, di[idx], alpha)
"""

def backProp_test():
    """
    Tests the back propagation algorithm with an arbitrary data set
    """

    # Interestingly, the NN convergers when the value is under 1. However,
    # occasionaly it will diverge and appproach positive or negative infinity.

    g = Graph()
    outputs = []
    target = [(0.0,0.0),(math.pi,1.0),(3*math.pi/2,-1.0)]
    alpha = .01
    MAX = 1000

    inputs = [g.add_node(i, kin='input', ix = float(i+1)) for i in range(3)]
    hidden = [g.add_node(i) for i in range(3,5)]
    output = g.add_node(5, kin='output')

    # To hidden
    for x,y in ((3,0),(4,0),(4,1),(4,2),(3,1),(3,2)):
        g.addEdge(x,y)

    # To output
    #for x,y in ((5,3),(5,4)):
    #    g.addEdge(x,y)
    g.addEdge(5,3,weight=round(random(),2))
    g.addEdge(5,4,weight=round(random(),2))

    di = [0 for i in range(len(hidden))]

  for i in range(MAX):
        for ind in target:
            for idx, outputWeight in enumerate(output.getConnections()):
                di[idx] = output.get_change(ind[0])
                updateOutputWeight(output, outputWeight, ind[0], alpha)

            for idx, hiddenNode in enumerate(hidden):
                for inputWeight in hiddenNode.getConnections():
                    updateHiddenWeight(hiddenNode, inputWeight, di[idx], alpha)

            # print 'output:', output.activate()
            outputs.append(output.activate())
            plt.plot(range(MAX), outputs, 'b-')
            del outputs[:]


    # Plot information
    plt.figure(1)
    plt.clf()
    plt.title('ANN Output Value Evolution')
    plt.ylabel('Output value')
    plt.xlabel('Epoch')
    plt.ylim(0,4)

    # Plot the target value line (trend should converge here)
    # plt.axhline(target, color='r')
    points = [i for i[0] in target]
    targs = [i for i[1] in target]
    print 'targs: ' + len(targs)
    print 'points: ' + len(points)

    # Plot the output node at each epoch
    plt.plot(range(MAX), outputs, 'b-')

     #plt.plot(points, targs, 'ro')

