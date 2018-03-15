import numpy as np
import math
 
inputNodes = 2
hiddenNodes = 2
outputNodes = 1

inputs = np.random.rand(inputNodes,1)
hidden = np.random.rand(hiddenNodes,1)
output = np.random.rand(outputNodes,1)
expected = np.random.rand(outputNodes,1)
 
rate = 0.02
 
weights_0_1 = np.random.rand(hiddenNodes,inputNodes)
weights_1_2 = np.random.rand(outputNodes,hiddenNodes)
 
bias_hid = np.random.rand(hiddenNodes,1)
bias_out = np.random.rand(outputNodes,1)

error = np.random.rand(outputNodes,1)

def relu(x):
    return np.maximum(0, x)
 
def drelu(x):
    return (x > 0).astype(np.float)
 
def forwardPropogation():
    global hidden, output
    hidden = weights_0_1.dot(inputs)
    hidden += bias_hid
    hidden = relu(hidden)
 
    output = np.matmul(weights_1_2,hidden)
    output = np.add(output, bias_out)
    output = relu(output)
 
def train():
    global weights_0_1, weights_1_2, bias_hid,bias_out,error

    forwardPropogation()
 
    error = expected- output
    gradient = output
    gradient = drelu(gradient)
    gradient = np.dot(gradient,error)
    gradient *= rate
   
    hidden_t = hidden.transpose()
    delta_hid = np.dot(gradient,hidden_t)

    weights_1_2 += delta_hid
    bias_out += gradient

    who_t = weights_1_2.transpose()
    hidden_error = np.dot(who_t,error)
    
    hidden_gradient = hidden
    hidden_gradient = drelu(hidden_gradient).transpose()
    hidden_gradient = np.matmul(hidden_gradient,hidden_error)
    hidden_gradient *= rate

    inputs_t = inputs.transpose()
    delta_in = np.dot(hidden_gradient,inputs_t)
    weights_0_1 += delta_in
    bias_hid += hidden_gradient
iterations = 30000
for x in range(iterations+4):
	
	if x%4==0:
		inputs = np.matrix([[0],[ 0]])
		expected = np.matrix([[0]])
	elif x%4==1:
		inputs = np.matrix([[0],[ 1]])
		expected = np.matrix([[1]])
	elif x%4==2:
		inputs = np.matrix([[1],[ 0]])
		expected = np.matrix([[1]])
	elif x%4==3:
		inputs = np.matrix([[1],[ 1]])
		expected = np.matrix([[0]])	
	
	train()
	if x >=iterations:
		print("expected: " + str(np.round(expected)) + " out:" + str(np.round(output))+ " error: " + str(error))
