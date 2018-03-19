import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
tf.__version__

mnist = input_data.read_data_sets("data/MNIST",one_hot=True)
batch_size = 100
LearningRate = 0.2


n_batch = mnist.train.num_examples//batch_size

x=tf.placeholder(tf.float32,[None,784])
y= tf.placeholder(tf.float32,[None,10])

W1 = tf.Variable(tf.random_normal([784,10],stddev=0.4))
B1 = tf.Variable(tf.zeros([10]))

prediction = tf.nn.softmax(tf.matmul(x,W1)+B1)

entropy = tf.nn.softmax_cross_entropy_with_logits(labels = y,logits=prediction)

loss = tf.reduce_mean(entropy)

train_step = tf.train.GradientDescentOptimizer(LearningRate).minimize(loss)

init = tf.global_variables_initializer()

correct_prediction = tf.equal(tf.argmax(y,1),tf.argmax(prediction,1))

accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))

with tf.Session() as sess:
	sess.run(init)
	for epoch in range(21):
		for batch in range(n_batch):
			batch_xs,batch_ys = mnist.train.next_batch(batch_size)
			sess.run(train_step,feed_dict = {x:batch_xs,y:batch_ys})
		acc=sess.run(accuracy,feed_dict={x:mnist.test.images,y:mnist.test.labels})
		print("Iteration: " + str(epoch) + " accuracy: " + str(acc))

