from node import *

class Graph:
    def __init__(self):
        self.nodeList = {}
        self.numNode = 0

    def addNode(self, key, kin='hidden', ix=0):
        self.numNode = self.numNode + 1
        newNode = Node(key, kind=kin, i=ix)
        self.nodeList[key] = newNode
        return newNode

    def getNode(self, n):
        if n in self.vertlist:
            return self.verList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.nodeList

    def addEdge(self, a, b, weight=0):
        if a not in self.nodeList:
            self.addNode(a)
        if b not in self.nodeList:
            self.addNode(b)

        self.nodeList[a].addConnection(self.nodeList[b], weight)

    def getNodes(self):
        return self.nodeList.keys()

    def __iter__(self):
        return iter(self.nodeList.values())

"""
def graph_test():
    ""
    Tests the functionality of the fundamental components of the
    Graph class.
    ""
    g = Graph()

    for i in range(6):
        g.addNode(i)

    g.getNodes()

    g.addEdge(0,1,.3)
    g.addEdge(1,3,.5)
    g.addEdge(4,5,.1)
    g.addEdge(2,4,.8)

    for v in g:
        for w in v.getConnections():
            print("( %s , %s )" % (v.getId(), w.getId()))

def activation_test():
    ""
    Test the activation function for the Node class
    ""

    g = Graph()

    for i in range(3):
        g.addNode(i, kin='input', ix = 2.)

    g.addNode(3)
    g.addNode(4)

    g.addEdge(3,0,weight=.3)
    g.addEdge(4,0,weight=.6)
    g.addEdge(3,1,weight=.7)
    g.addEdge(3,2,weight=.4)

    print [node.activate() for node in g]
    print [node.dActivate() for node in g]

"""
