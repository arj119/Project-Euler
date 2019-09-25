#Training data
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

import tensorflow as tf

# Turning image data into a 2D array with each 28x28 image represented as 784 array.
#Also None in this instance represents that the array can be of any number of rows
x = tf.placeholder(tf.float32, [None, 784])

#Creating weight variable as a compatible matrix array for multiplication.
W = tf.Variable(tf.zeros([784,10]))
#Creating a bias variable as a compatible matrix for addition
b = tf.Variable(tf.zeros([10]))

#Carrying out softmax regression on data in form y= Wx + b
y = tf.nn.softmax(tf.matmul(x,W) + b)

#Loss/ Cost for evaluation of training
y_ = tf.placeholder(tf.float32, [None, 10])
#Cross entropy calculation
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))

train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

sess = tf.InteractiveSession()
tf.global_variables_initializer().run()

#Run training data
for _ in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict = {x: batchxs, y: batchyx})

correctPrediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correctPrediction, tf.float32))

print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))

    
             

