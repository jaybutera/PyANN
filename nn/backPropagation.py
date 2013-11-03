import json
from graph import *
from node import *
import matplotlib.pyplot as plt
from random import random

def backProp_test():
    """
    Tests the back propagation algorithm with an arbitrary data set
    """

    g = Graph()
    outputs = []
    target = [(0.0,0.0),(math.pi,1.0),(3*math.pi/2,-1.0)]
    x_target = [point[0] for point in target]
    alpha = (max(x_target) - min(x_target))/len(target)
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

    # Perform backpropagation through MAX epochs
    for i in range(MAX):
        # Iterate through all training set points in target
        for ind in target:
            # Calculate and modify output layer values
            for idx, output_weight in enumerate(output.get_connections()):
                output.delta_i = output.get_change(ind[0])
                output.update_weight(output_weight, ind[0], alpha)

            # Calculate and modify hidden layer values
            for idx, hidden_node in enumerate(hidden):
                for inputWeight in hidden_node.get_connections():
                    hidden_node.update_weight(inputWeight,
                            hidden_node.delta_i, alpha)

            # Accumulate output node values of every cycle
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

    # Plot the output node at each cycle
    plt.plot(range(len(target)*MAX), outputs, 'b-')
    plt.plot([999,1999,2999], targs, 'ro')

    # Use this once graphing an unsupervised learning environment
    # plt.plot(points, targs, 'ro')
    plt.show()

