from graph import *

# Evenutally merge these two update weight functions to work with both output
# and hidden nodes.
def updateOutputWeight(node, lower, targ, alpha):
    node.setWeight(lower, node.getWeight(lower) + alpha * node.activate() * node.getChange(targ))

def updateHiddenWeight(node, lower, di, alpha):
    node.setDi(di)
    node.setWeight(lower, node.getWeight(lower) + alpha * node.activate() * node.getChange())

def backProp_test():
    """
    Tests the back propagation algorithm with an arbitrary data set
    """

    g = Graph()
    target = 3.
    alpha = .01

    inputs = [g.addNode(i, kin='input', ix = float(i+1)) for i in range(3)]
    hidden = [g.addNode(i) for i in range(3,5)]
    output = g.addNode(5, kin='output')

    # To hidden
    g.addEdge(3,0,weight=.3)
    g.addEdge(4,0,weight=.6)
    g.addEdge(4,1,weight=.4)
    g.addEdge(4,2,weight=.2)
    g.addEdge(3,1,weight=.7)
    g.addEdge(3,2,weight=.4)

    # To output
    g.addEdge(5,3,weight=.5)
    g.addEdge(5,4,weight=.8)

    # I hope you're ashamed of yourself. Shun yourself for the ugly code that
    # is below this comment
    di = [0 for i in range(len(hidden))]

    for i in range(100):
        j=0
        for outputWeight in output.getConnections():
            di[j] = output.getChange(target)
            updateOutputWeight(output, outputWeight, target, alpha)
            print di
            j+=1

        j=0
        for hiddenNode in hidden:
            for inputWeight in hiddenNode.getConnections():
                updateHiddenWeight(hiddenNode, inputWeight, di[j], alpha)
            j+=1

        print 'output: ' + output.activate()
