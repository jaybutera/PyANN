PyANN
=====

An execution of a generic artificial neural network written in Python2.7.
Analytics are done in matplotlib. The goal of the project is 
to help understand the process of learning through continous epochs in 
an artificial neural network.

###Methods of supervised learning:
- Backpropagation

###Goals:
- Support for both feed-forward and recurrent networks
- Browswer visualization of neural network in action
- Neuroevolution algorithm implementations
- Network encoded with JSON

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
