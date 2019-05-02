import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("/tmp/data/", one_hot=True)

LEARNING_RATE = 0.001
EPOCHS = 15
BATCH_SIZE = 100
STEP = 1
NROFCLASSES = 10

X = tf.placeholder("float", [None, 28*28*1])
Y = tf.placeholder("float", [None, NROFCLASSES])
weights = {
    'h1': tf.Variable(tf.random_normal([28*28*1, 256])),
    'h2': tf.Variable(tf.random_normal([256, 256])),
    'out': tf.Variable(tf.random_normal([256, NROFCLASSES]))}
biases = {
    'b1': tf.Variable(tf.random_normal([256])),
    'b2': tf.Variable(tf.random_normal([256])),
    'out': tf.Variable(tf.random_normal([NROFCLASSES]))}

def multilayer_perceptron(input_data):
    net = tf.add(tf.matmul(input_data, weights['h1']), biases['b1'])
    net = tf.add(tf.matmul(net, weights['h2']), biases['b2'])
    logits = tf.matmul(net, weights['out']) + biases['out']
    return logits

def build_network(input_data):
    logits = multilayer_perceptron(input_data)
    loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=logits, labels=Y))
    return loss, logits

def train():
    loss, logits = build_network(X)
    optimizer = tf.train.AdamOptimizer(learning_rate=LEARNING_RATE)
    train_ops = optimizer.minimize(loss)
    init = tf.global_variables_initializer()
    with tf.Session() as sess:
        sess.run(init)
        for epoch in range(EPOCHS):
            avg_cost = 0.
            total_batch = int(mnist.train.num_examples/BATCH_SIZE)
            for i in range(total_batch):
                batch_x, batch_y = mnist.train.next_batch(BATCH_SIZE)
                train_loss, _ = sess.run([loss, train_ops], feed_dict={X: batch_x, Y: batch_y})
                avg_cost += train_loss / total_batch
            if epoch % STEP == 0:
                print('Epoch: {}, Avg Cost: {}, Train Loss: {}'.format(epoch+1, avg_cost, train_loss))
        pred = tf.nn.softmax(logits)
        correct_prediction = tf.equal(tf.argmax(pred, 1), tf.argmax(Y, 1))
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
        print("Accuracy:", accuracy.eval({X: mnist.test.images, Y: mnist.test.labels}))

if __name__ == "__main__":
    train()
