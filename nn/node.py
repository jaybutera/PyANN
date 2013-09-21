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
        if self.kind == 'output':
            return (target-self.activate()) * self.dActivate()
        elif self.kind == 'hidden':
            return self.dActivate() * sum([self.getWeight(i)*self.di for i in self.getConnections()])

    def getDi(self):
        return self.di

    def setDi(self, _di):
        self.di = _di

    def addConnection(self, nbr, weight=0.):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connected to: ' + str([elem.id for elem in
            self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, node):
        return self.connectedTo[node]

    def setWeight(self, node, weight):
        self.connectedTo[node] = weight

    def sigmoid(self, a):
        return (1/(1+math.exp(-a)))

    def dActivate(self):
        if self.kind== 'input':
            return self.val
#        elif self.kind == 'hidden':
        else:
            x = self.activate()
            return (x * (1-x))

    def activate(self):
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

