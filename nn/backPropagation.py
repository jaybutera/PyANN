from graph import *
from node import * # Eventually only interface to nodes through graph
import matplotlib.pyplot as plt
from random import random
from fileToMatrix import get_data

def run_layer(layer):
    for idx, node in enumerate(layer):
        for weight in node.get_connections():
            node.update_weight(weight, node.delta_i, alpha)

def backProp_test():
    """
    Tests the back propagation algorithm with an arbitrary data set
    """

    g = Graph()
    outputs = []
    #target = [(0.0, 0.0),(math.pi/2, 1.0), (math.pi, 0.0), (3*math.pi/2, -1.0), (2*math.pi, 0)]
    # Modify filepath
    #target = get_data('/Users/jaybutera/Documents/Programming/PyANN/datasets/fmtrain.dat')
    target = [(x,0) for x in range(-50,50)]
    x_target = [point[0] for point in target]
    y_target = [i[0] for i in target]
    alpha = (max(x_target) - min(x_target))/len(target)
    MAX = 1

    inputs = g.add_input_node(0)
    #hidden = [g.add_hidden_node(i) for i in range(1, 3)]
    output = g.add_output_node(3)

    # To hidden
    #for x, y in ((1,0), (2,0)):
    #    g.add_edge(x,y)

    # To output
    #for x, y in ((3, 1), (3, 2)):
    #    g.add_edge(x, y)

    g.add_edge(3, 0)

    # Perform backpropagation through MAX epochs
    for i in range(MAX):
        outputs = []
        for ind in target:
    '''
    for i in range(MAX):
        # Iterate through all training set points in target
        outputs = []
        for ind in target:
            # Update input nodes
            inputs.val = ind[0]
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

    '''
    # Plot information
    plt.figure(0)
    plt.clf()
    plt.title('ANN Output Value Evolution')
    plt.ylabel('Output value')
    plt.xlabel('Epoch')
    plt.ylim(-2, 2)

    # Plot the target value line (trend should converge here)
    plt.plot(x_target, y_target, 'ro')

    # Plot the output node at each cycle
    plt.plot(x_target, outputs, 'b-')

    # Use this once graphing an unsupervised learning environment
    plt.show()
