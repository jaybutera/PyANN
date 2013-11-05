import math
from random import random

class Node(object):
    def __init__(self):
        raise NotImplementedError()

    def get_weight(self, node):
        """
        Returns the weight between itself
        and the specified node.
        """
        return self.connectedTo[node]

    def set_weight(self, node, weight):
        """
        Sets the weight between itself
        and the specified node.
        """
        self.connectedTo[node] = weight

    def add_connection(self, nbr, weight=round(random(), 2)):
        """
        Connects a separate node instance of a specified
        weight (default random) to the node.
        """
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.key) + ' connected to: ' + str([elem.key for elem in
            self.connectedTo])

    def get_connections(self):
        """
        Returns a list of all node instances
        that are connected to it.
        """
        return self.connectedTo.keys()

    def sigmoid(self, a):
        """
        Returns the sigmoid function mappng of
        the specified input. Serves as a form
        of activation function.
        """
        return (1/(1+math.exp(-a)))

class InputNode(Node):
    def __init__(self, key, i_val=0.):
        self.key = key
        self.val = i_val
        self.connectedTo = {}

    def activate(self):
        return self.val

    def dActivate(self):
        return self.val

class HiddenNode(Node):
    def __init__(self, key):
        self.key = key
        self.connectedTo = {}
        self.delta_i = 0.

    def get_change(self):
        return self.dActivate() * sum([self.get_weight(i)*self.delta_i for i in self.get_connections()])

    def update_weight(self, lower, delta_i, alpha):
        self.delta_i = delta_i
        self.set_weight(lower, self.get_weight(lower) + alpha * self.activate() *
                self.get_change())

    def activate(self):
        a=0

        for node in self.connectedTo.keys():
            a += node.activate() * self.get_weight(node)
        return self.sigmoid(a)

    def dActivate(self):
        x = self.activate()
        return (x * (1-x))

class OutputNode(Node):
    def __init__(self, key):
        self.key = key
        self.connectedTo = {}
        self.delta_i = 0.

    def get_change(self, target):
        return (target-self.activate()) * self.dActivate()

    def update_weight(self, lower, target, alpha):
        self.set_weight(lower, self.get_weight(lower) +
                alpha * self.activate() * self.get_change(target))

    def activate(self):
        a=0

        for node in self.connectedTo.keys():
            a += node.activate() * self.get_weight(node)
        return a

    def dActivate(self):
        x = self.activate()
        return (x * (1-x))

