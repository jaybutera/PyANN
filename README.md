PyANN
=====

An execution of a generic artificial neural network written in Python2.7.
Analytics plotting and visualization is done in d3.js. The goal of the project is
to help understand the how ANNs work, and the effect of varying topologies for learning
through continous epochs in an artificial neural network.

###Methods of supervised learning:
- Backpropagation

###Goals:
- [ ] Fully generic network with variable number of input nodes, output nodes, and layers.
- [ ] Interactive and visual network topology building and modification mode.
- [ ] Visualization of neural network learning ouptput on specified data set.
- [ ] Access state vector at any point (pickled).

###Dependencies
# Soon to be removed
- Matplotlib

Perform the following command to use the dependencies file.
```
pip install -r requirements.txt
```

###Testing:
To simplify the use of test functions, use nosetests (downloaded with pip or
easy-install). Use the following line to run the backpropagation test
function:

```
pip install nosetests
nosetests backPropagation.py
```
