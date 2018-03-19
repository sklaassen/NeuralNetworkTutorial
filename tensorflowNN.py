import tensorflow as tf
import numpy as np

tf.__version__

inputNodes = 2
hiddenNodes = 5
outputNodes = 1
learningrate = 0.01

inputData = [[0,0],[0,1],[1,0],[1,1]]
predictData = [[0],[1],[1],[0]]

x = tf.placeholder(tf.float32,[4,inputNodes])
y = tf.placeholder(tf.float32,[4,outputNodes])

weights_hidden = tf.Variable(tf.random_uniform([inputNodes,hiddenNodes], -1,1))
bias_hidden = tf.Variable(tf.zeros([hiddenNodes]))
weights_output = tf.Variable(tf.random_uniform([hiddenNodes,outputNodes], -1,1))
bias_output = tf.Variable(tf.zeros([outputNodes]))

lossHidden = tf.nn.leaky_relu(tf.matmul(x,weights_hidden)+bias_hidden)
prediction = tf.nn.leaky_relu(tf.matmul(lossHidden, weights_output) + bias_output)

error = tf.nn.l2_loss(prediction - y)

#train_step = tf.train.GradientDescentOptimizer(learningrate).minimize(error)
train_step = tf.train.AdamOptimizer(learningrate).minimize(error)

init = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init)

numberEpochs = 10000
for epoch in range(numberEpochs):
    train,predict = sess.run([train_step,prediction], feed_dict = {x : inputData,y : predictData})

    print("training[" + str(int(epoch/numberEpochs*1000)/10) + "%]" + str(abs(predict.round()).transpose()[0]),end='\r')
        
predict = sess.run(prediction, feed_dict = {x :inputData, y : predictData})
print("predict: " + str(abs(predict.round()).transpose()[0])+ " actual: " + str(predictData))