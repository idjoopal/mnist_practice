import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# mnist 데이터셋
mnist = input_data.read_data_sets('MNIST_data/', one_hot=True)

# 회귀 구현
x = tf.placeholder(tf.float32, [None, 784])
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

y = tf.nn.softmax(tf.matmul(x, W) + b)

# 학습
y_ = tf.placeholder(tf.float32, [None, 10])
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))

train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

# 학습 실행
init = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init)

# 학습 데이터셋에서 무작위 100개(batch)를 가져온다
# 확률적 경사 하강법
for i in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

# 모델 평가
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

# 정확도 출력
print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))