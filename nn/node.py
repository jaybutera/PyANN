import math

class Node:
    def __init__(self, key, kind='hidden', i=0.):
        self.id = key
        self.di = 0.
        self.kind = kind
        if self.kind == 'input':
            self.val = i
        self.connectedTo = {}

    def getChange(self, target=None):
        """
        Returns the change in weight values.
        """
        if self.kind == 'output':
            return (target-self.activate()) * self.dActivate()
        elif self.kind == 'hidden':
            return self.dActivate() * sum([self.getWeight(i)*self.di for i in self.getConnections()])

    def getDi(self):
        """
        Returns the node's deltaI value from the
        previous weight update.
        """
        return self.di

    def setDi(self, _di):
        """
        Set the error of the node's output times
        the derivative of the activation function.
        Referred to as deltaI.
        """
        self.di = _di

    def addConnection(self, nbr, weight=0.):
        """
        Connects a separate node instance of a specified
        weight (default 0.0) to the node.
        """
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connected to: ' + str([elem.id for elem in
            self.connectedTo])

    def getConnections(self):
        """
        Returns a list of all node instances
        that are connected to it.
        """
        return self.connectedTo.keys()

    def getId(self):
        """
        Returns node ID.
        """
        return self.id

    def getWeight(self, node):
        """
        Returns the weight between itself
        and the specified node.
        """
        return self.connectedTo[node]

    def setWeight(self, node, weight):
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

    def activate(self):
        """
        Returns the value of the sum of connected
        nodes' output values * the corresponding
        weights fed into the sigmoid function.
        """
        if self.kind == 'input':
            return self.val
        elif self.kind == 'hidden':
            a=0

            for node in self.connectedTo.keys():
                a += node.activate() * self.getWeight(node)
            return self.sigmoid(a)
        elif self.kind == 'output':
            a=0

            for node in self.connectedTo.keys():
                a += node.activate() * self.getWeight(node)
            return a
        else:
            return None

    def dActivate(self):
        """
        Returns the derivative of the activation
        function. If the node is of type input,
        the value remains the same.
        """
        if self.kind== 'input':
            return self.val
        else:
            x = self.activate()
            return (x * (1-x))

