import json
from graph import *
from node import *
import matplotlib.pyplot as plt
from random import random

# Evenutally merge these two update weight functions to work with both output
# and hidden nodes.
def updateOutputWeight(node, lower, targ, alpha):
    node.set_weight(lower, node.get_weight(lower) + alpha * node.activate() * node.get_change(targ))

def updateHiddenWeight(node, lower, delta_i, alpha):
    node.set_delta_i(delta_i)
    node.set_weight(lower, node.get_weight(lower) + alpha * node.activate() * node.get_change())

"""
def run(filepath):
    ""
    Runs a specified network via JSON with
    a specified number of epochs.
    ""
    g = Graph()

    for i in range(MAX):
        for ind in target:
            for idx, outputWeight in enumerate(output.get_connections()):
                delta_i[idx] = output.get_change(ind[1])
                updateOutputWeight(output, outputWeight, ind[1], alpha)

            for idx, hiddenNode in enumerate(hidden):
                for inputWeight in hiddenNode.get_connections():
                    updateHiddenWeight(hiddenNode, inputWeight, delta_i[idx], alpha)
"""

def backProp_test():
    """
    Tests the back propagation algorithm with an arbitrary data set
    """

    g = Graph()
    outputs = []
    target = [(0.0,0.0),(math.pi,1.0),(3*math.pi/2,-1.0)]
    alpha = .01
    MAX = 1000

    #inputs = [g.add_node(i, kin='input', ix = float(i+1)) for i in range(3)]
    inputs = [g.add_input_node(i,float(i+1)) for i in range(3)]
    hidden = [g.add_hidden_node(i) for i in range(3,5)]
    output = g.add_output_node(5)

    # To hidden
    for x,y in ((3,0),(4,0),(4,1),(4,2),(3,1),(3,2)):
        g.add_edge(x,y)

    # To output
    for x,y in ((5,3),(5,4)):
        g.add_edge(x,y)

    delta_i = [0 for i in hidden]

    for i in range(MAX):
        for ind in target:
            for idx, outputWeight in enumerate(output.get_connections()):
                delta_i[idx] = output.get_change(ind[0])
                updateOutputWeight(output, outputWeight, ind[0], alpha)

            for idx, hiddenNode in enumerate(hidden):
                for inputWeight in hiddenNode.get_connections():
                    updateHiddenWeight(hiddenNode, inputWeight, delta_i[idx], alpha)

            outputs.append(output.activate())

    # Plot information
    plt.figure(0)
    plt.clf()
    plt.title('ANN Output Value Evolution')
    plt.ylabel('Output value')
    plt.xlabel('Epoch')
    plt.ylim(-2,2)

    # Plot the target value line (trend should converge here)
    points = [i[0] for i in target]
    targs = [i[1] for i in target]
    #print 'targs: ' + len(targs)
    #print 'points: ' + len(points)

    # Plot the output node at each epoch
    plt.plot(range(len(target)*MAX), outputs, 'b-')
    plt.plot([999,1999,2999], targs, 'ro')

    # Use this once graphing an unsupervised learning environment
    # plt.plot(points, targs, 'ro')
    plt.show()

