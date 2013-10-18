from node import *
import json

class Graph:
    def __init__(self):
        self.nodeList = {}
        self.numNode = 0

    def add_node(self, key, kin='hidden', ix=0):
        """
        Adds a node of any type with no initial
        connections to the graph.
        """
        self.numNode = self.numNode + 1
        newNode = Node(key, kind=kin, i=ix)
        self.nodeList[key] = newNode
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
        return n in self.nodeList

    def add_edge(self, a, b, weight=0):
        """
        Adds an undirected edge of a specified
        weight between node IDs a and b. If a
        or b does not exist, they will be initialed
        prior to edge placement.
        """
        if a not in self.nodeList:
            self.add_node(a)
        if b not in self.nodeList:
            self.add_node(b)

        self.nodeList[a].add_connection(self.nodeList[b], weight)

    def get_nodes(self):
        """
        Returns a list of all node IDs that
        exist in the graph.
        """
        return self.nodeList.keys()

    def __iter__(self):
        return iter(self.nodeList.values())

def graph_test():
    """
    Tests the functionality of the fundamental components of the
    Graph class.
    """
    g = Graph()

    for i in range(6):
        g.add_node(i)

    g.get_nodes()

    for x,y in ((0,1),(1,3),(4,5),(2,4)):
        g.add_edge(x,y)

    for v in g:
        for w in v.get_connections():
            print("( %s , %s )" % (v.get_id(), w.get_id()))

def activation_test():
    """
    Test the activation function for the Node class
    """

    g = Graph()

    for i in range(3):
        g.add_node(i, kin='input', ix = 2.)

    g.add_node(3)
    g.add_node(4)

    for x,y in ((3,0),(4,0),(3,1),(3,2)):
        g.add_edge(x,y)

    print [node.activate() for node in g]
    print [node.dActivate() for node in g]

class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if not isinstance(obj, Tree):
            return super(MyEncoder, self).default(obj)

        return obj.__dict__

