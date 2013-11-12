from node import *

class Layer:
    key = 0
    def __init__(self, num):
        raise NotImplementedError

    def get_node(self, n):
        """
        Returns the instance of the specified
        node ID. If the node does not exist,
        returns None.
        """

        if n in self.vertlist:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.node_dict

    def __iter__(self):
        return iter(self.node_dict.values())

    def add_edge(self, a, b, weight=round(random(), 2)):
        """
        Adds an undirected edge of a specified
        weight between node IDs a and b. If a
        or b does not exist, they will be initialed
        prior to edge placement. Networks abide by
        a backward directed connectivity scheme.
        """

        if a < b:
            print 'connection should be directed backward, not forward'
            self.add_edge(b, a, weight)

        if a not in self.node_dict:
            t = type(a)
            if t == InputNode:
                self.add_input_node(a)
            elif t == HiddenNode:
                self.add_hidden_node(a)
            elif t == OutputNode:
                self.add_output_node(a)
            else:
                raise TypeError
        if b not in self.node_dict:
            t = type(b)
            if t == InputNode:
                self.add_input_node(a)
            elif t == HiddenNode:
                self.add_hidden_node(a)
            elif t == OutputNode:
                self.add_output_node(a)
            else:
                raise TypeError

        self.node_dict[a].add_connection(self.node_dict[b], weight)

    def get_nodes(self):
        """
        Returns a list of all node IDs that
        exist in the graph.
        """
        return self.node_dict.keys()

class InputLayer(Layer):
    def __init__(self, num=0):
        # Set layer key
        self.key = Test.key
        Test.key += 1
        # Initialize node list in layer
        self.node_dict = {}
        [add_input_node(i) for i in range(self.key, self.key+num)]
        # Initiate layer's node count
        self.numNode = 0

    def add_input_node(self, key, i_val=0.):
        """
        Adds an input node with no initial
        connections to the graph.
        """
        self.numNode = self.numNode + 1
        newNode = InputNode(key, i_val)
        self.node_dict[key] = newNode

class HiddenLayer(Layer):
    def __init__(self, num=0):
        # Set layer key
        self.key = Test.key
        Test.key += 1
        # Initialize node list in layer
        self.node_dict = {}
        [add_hidden_node(i) for i in range(self.key, self.key+num)]
        # Initiate layer's node count
        self.numNode = 0

    def add_hidden_node(self, key):
        """
        Adds an hidden node with no initial
        connections to the graph.
        """
        self.numNode = self.numNode + 1
        newNode = HiddenNode(key)
        self.node_dict[key] = newNode

class OutputLayer(Layer):
    def __init__(self, num=0):
        # Set layer key
        self.key = Test.key
        Test.key += 1
        # Initialize node list in layer
        self.node_dict = {}
        [add_output_node(i) for i in range(self.key, self.key+num)]
        # Initiate layer's node count
        self.numNode = 0

    def add_output_node(self, key):
        """
        Adds an output node with no initial
        connections to the graph.
        """
        self.numNode = self.numNode + 1
        newNode = OutputNode(key)
        self.node_dict[key] = newNode

