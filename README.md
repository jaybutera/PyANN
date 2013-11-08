PyANN
=====

An execution of a generic artificial neural network written in Python2.7.
Analytics plotting is done in d3.js. The goal of the project is
to help understand the process of learning through continous epochs in
an artificial neural network.

###Methods of supervised learning:
- Backpropagation

###Goals:
- Support for both feed-forward and recurrent networks
- Browswr visualization of neural network topology and learning ouptput in action
- Neuroevolution algorithm implementations
- Access state vector at any point (pickled)

###Dependencies
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
