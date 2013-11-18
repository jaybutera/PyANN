from layer import *
import matplotlib.pyplot as plt
from random import random
from fileToMatrix import get_data

def backProp_test(inputs, hidden = None, output, target, MAX):
    """
    Tests the back propagation algorithm with an arbitrary data set
    """

    x_target = [point[0] for point in target]
    y_target = [i[0] for i in target]
    alpha = (max(x_target) - min(x_target))/len(target)

    # Perform backpropagation through MAX epochs
    for i in range(MAX):
        outputs = []
        for ind in target:
            # Update input nodes
            update_nodes(ind[:-1])

            # Calculate and modify output layer values
            output.run_layer()
            # Calculate and modify hidden layer values
            for layer in hidden:
                layer.run_layer()

            outputs.append(o)

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
