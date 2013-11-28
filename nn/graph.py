from layer import *
from backPropagation import *

class Graph:
    def __init__(self):
        self.layer_dict = {}
        self.num_layer = 0

    def add_input_layer(self, num):
        self.num_layer += 1
        new_layer = InputLayer(num)
        self.layer_dict[new_layer.key] = new_layer

        return new_layer

    def add_hidden_layer(self, num):
        self.num_layer += 1
        new_layer = HiddenLayer(num)
        self.layer_dict[new_layer.key] = new_layer

        return new_layer

    def add_output_layer(self, num):
        self.num_layer += 1
        new_layer = OutputLayer(num)
        self.layer_dict[new_layer.key] = new_layer

        return new_layer

g = Graph()
outputs = []
#target = [(0.0, 0.0),(math.pi/2, 1.0), (math.pi, 0.0), (3*math.pi/2, -1.0), (2*math.pi, 0)]
# Modify filepath
#target = get_data('/Users/jaybutera/Documents/Programming/PyANN/datasets/fmtrain.dat')
target = [(x,0) for x in range(-50,50)]
MAX = 1

inputs = g.add_input_layer(1)
print 'input nodes: ', inputs.get_nodes()
hidden = g.add_hidden_layer(2)
print 'hidden nodes: ', hidden.get_nodes()
output = g.add_output_layer(1)
print 'output nodes: ', output.get_nodes()

# To hidden
for x, y in ((1,0), (2,0)):
    hidden.add_edge(x,y)

# To output
for x, y in ((3, 1), (3, 2)):
    output.add_edge(x, y)

#output.add_edge(1, 0)

backProp_test(inputs, output, target, MAX)
