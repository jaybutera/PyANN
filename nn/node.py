import math
from random import random

class Node:
    def __init__(self, key, kind='hidden', i=0.):
        raise NotImplementedError()

    """
    def get_change(self, target=None):
        Returns the change in weight values.
        if self.kind == 'output':
            return (target-self.activate()) * self.dActivate()
        elif self.kind == 'hidden':
            return self.dActivate() * sum([self.get_weight(i)*self.delta_i for i in self.get_connections()])
    """

    # Deprecate
    def get_delta_i(self):
        """
        Returns the node's deltaI value from the
        previous weight update.
        """
        return self.delta_i

    # Deprecate
    def set_delta_i(self, delta_i):
        """
        Set the error of the node's output times
        the derivative of the activation function.
        Referred to as deltaI.
        """
        self.delta_i = delta_i

    def add_connection(self, nbr, weight=round(random(),2)):
        """
        Connects a separate node instance of a specified
        weight (default 0.0) to the node.
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

    # Deprecate
    def get_id(self):
        """
        Returns node ID.
        """
        return self.key

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

    def sigmoid(self, a):
        """
        Returns the sigmoid function mappng of
        the specified input. Serves as a form
        of activation function.
        """
        return (1/(1+math.exp(-a)))

    """
    def activate(self):
        Returns the value of the sum of connected
        nodes' output values * the correspondelta_ing
        weights fed into the sigmoid function.
        if self.kind == 'input':
            return self.val
        elif self.kind == 'hidden':
            a=0

            for node in self.connectedTo.keys():
                a += node.activate() * self.get_weight(node)
            return self.sigmoid(a)
        elif self.kind == 'output':
            a=0

            for node in self.connectedTo.keys():
                a += node.activate() * self.get_weight(node)
            return a
        else:
            return None

    def dActivate(self):
        Returns the derivative of the activation
        function. If the node is of type input,
        the value remains the same.
        if self.kind== 'input':
            return self.val
        else:
            x = self.activate()
            return (x * (1-x))
     """

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

    def get_change(self, target=None):
        return self.dActivate() * sum([self.get_weight(i)*self.delta_i for i in self.get_connections()])

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

    def get_change(self, target=None):
        return (target-self.activate()) * self.dActivate()

    def activate(self):
        a=0

        for node in self.connectedTo.keys():
            a += node.activate() * self.get_weight(node)
        return a

    def dActivate(self):
        x = self.activate()
        return (x * (1-x))

