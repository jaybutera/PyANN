from node import *
import json

class Graph:
    def __init__(self):
        self.node_dict = {}
        self.numNode = 0

    def add_input_node(self, key, i_val=0):
        """
        Adds an input node with no initial
        connections to the graph.
        """
        self.numNode = self.numNode + 1
        newNode = InputNode(key, i_val)
        self.node_dict[key] = newNode
        return newNode

    def add_hidden_node(self, key):
        """
        Adds an hidden node with no initial
        connections to the graph.
        """
        self.numNode = self.numNode + 1
        newNode = HiddenNode(key)
        self.node_dict[key] = newNode
        return newNode

    def add_output_node(self, key):
        """
        Adds an output node with no initial
        connections to the graph.
        """
        self.numNode = self.numNode + 1
        newNode = OutputNode(key)
        self.node_dict[key] = newNode
        return newNode

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

    def add_edge(self, a, b, weight=0):
        """
        Adds an undirected edge of a specified
        weight between node IDs a and b. If a
        or b does not exist, they will be initialed
        prior to edge placement. Networks abide by
        a backward directed connectivity scheme.
        """

        if a < b:
            print 'connection should be directed backward, not forward'
            self.add_edge(b,a,weight)

        if a not in self.node_dict:
            self.add_node(a)
        if b not in self.node_dict:
            self.add_node(b)

        self.node_dict[a].add_connection(self.node_dict[b], weight)

    def get_nodes(self):
        """
        Returns a list of all node IDs that
        exist in the graph.
        """
        return self.node_dict.keys()

    def __iter__(self):
        return iter(self.node_dict.values())

