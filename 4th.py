
"""
Created on Mon Nov 26 10:43:41 2018

@author: prateek
"""

import numpy as np
from sklearn.datasets import load_iris


def sigmoid(z):
    s = 1/(1+(1/np.exp(z)))
    return s


iris_dataset=load_iris()
X=iris_dataset["data"][:-50,:] #am only taking two classes to keep the code simple
y= iris_dataset["target"].reshape(150,-1)[:-50,:] 


X=X.T
y=y.T

#i didn't split it into tarin/test 

num_iterations=2000
costs = []

n_x =np.size(X,axis=0)   # size of input layer
n_h=45       # size of hidden layer
n_y=1     # size of output layer


#random weights assigned
W1 = np.random.randn(n_h,n_x) *0.01
b1 = np.zeros((n_h,1))
W2 = np.random.randn(n_y,n_h) *0.01
b2 = np.zeros((n_y,1))



for i in range(0, num_iterations):
# Implement Forward Propagation to calculate A2 (probabilities)
    Z1 =np.array(np.dot(W1,X),dtype=np.float32)+b1
    A1 = np.tanh(Z1)
    Z2 = np.array(np.dot(W2,A1),dtype=np.float32)+b2
    A2 = sigmoid(Z2)
    
    #compute cost
    m = y.shape[1] # number of example
    logprobs = np.multiply(np.log(A2),y)+np.multiply(np.log(1-A2),(1-y))
    cost = -np.sum(logprobs)/m
    cost = np.squeeze(cost)
    
    
    if i % 10 == 0:  #to demonstrate on graph
        costs.append(cost)
           
    if i % 10 == 0:  #to print cost
        print ("Cost after iteration %i: %f" %(i, cost))
      
    #backprop
    dZ2 = A2-y
    dW2 = np.dot(dZ2,A1.T)/m
    db2 = np.sum(dZ2,axis=1,keepdims=True)/m
    dZ1 = np.dot(W2.T,dZ2)*(1 - np.power(A1, 2))
    dW1 = np.dot(dZ1, X.T) / m
    db1 = np.sum(dZ1, axis=1, keepdims=True) / m
    
    
    learning_rate=0.01
    W1 = W1-learning_rate*dW1
    b1 = b1-learning_rate*db1
    W2 = W2-learning_rate*dW2
    b2 = b2-learning_rate*db2
    
    
predictions=A2>0.4

from sklearn.metrics import accuracy_score
accuracy=accuracy_score(y,predictions)
print(accuracy)

#optional
import matplotlib.pyplot as plt
fig = plt.figure()
plt.plot(costs)
plt.ylabel('cost')
plt.xlabel('iterations (per hundreds)')
plt.title("Learning rate =0.01")













