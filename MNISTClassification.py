import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
tf.__version__

#imports all the data into a Matrix where the 2d image is broken down to a 1D vector
mnist = input_data.read_data_sets("data/MNIST",one_hot=True)
batch_size = 100
LearningRate = 0.2

#say hou many batches there are. // means a integer division
n_batch = mnist.train.num_examples//batch_size

#setting up the input and outputs
x=tf.placeholder(tf.float32,[None,784])
y= tf.placeholder(tf.float32,[None,10])

#setting up the weights and Bias
W1 = tf.Variable(tf.random_normal([784,10],stddev=0.4))
B1 = tf.Variable(tf.zeros([10]))

#define the prediction equation
prediction = tf.nn.softmax(tf.matmul(x,W1)+B1)

#define the entropy ("how wrong was the prediction")
entropy = tf.nn.softmax_cross_entropy_with_logits(labels = y,logits=prediction)

#reduce the size of the mean diffrence between the correct answer and the prediction
loss = tf.reduce_mean(entropy)

#LEARN!! thank god we dont have to program this
train_step = tf.train.GradientDescentOptimizer(LearningRate).minimize(loss)

#store the initialization to be called later
init = tf.global_variables_initializer()

#some meathods to see how well the neural networks with test images
correct_prediction = tf.equal(tf.argmax(y,1),tf.argmax(prediction,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))

#start a session
with tf.Session() as sess:
	#initalises all the predetermined variables and meathods
	sess.run(init)

	#loop through training data 21 times
	for epoch in range(21):
		acc=sess.run(accuracy,feed_dict={x:mnist.test.images,y:mnist.test.labels})
		print("Iteration: " + str(epoch) + " accuracy: " + str(acc))		
		#loop through training data in batches
		for batch in range(n_batch):
			#prepare the data to be inputed
			batch_xs,batch_ys = mnist.train.next_batch(batch_size)
			#run the code to learn
			sess.run(train_step,feed_dict = {x:batch_xs,y:batch_ys})
		#check how well the network is predicting


