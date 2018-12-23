
'''
https://www.slideshare.net/jaepilko10/ss-100430211
'''
import numpy as np
import tensorflow as tf

np.random.seed(0)
x = tf.placeholder(tf.float32, shape = (4, 2))
y = tf.placeholder(tf.float32, shape = (4, 1))
w = tf.placeholder(tf.float32, shape = (2, 1))
b = tf.placeholder(tf.float32)

y_pred = tf.matmul(x,w) + b
loss = 0.5 * tf.reduce_mean ((y - y_pred) * (y - y_pred))
grad_w, grad_b = tf.gradients(loss, [w, b])

values = {
    x: [[-1, -1], [-1, 1], [1, -1], [1, 1]],
    y: [[0], [1], [1], [1]],
    w: np.random.randn(2, 1),
    b: np.random.randn(1)
}

with tf.Session() as sess:
    learning_rate = 0.1
    for i in range(100):
        loss_v, grad_w_v, grad_b_v = sess.run([loss, grad_w, grad_b],
                                              feed_dict = values)
        values[w] -= learning_rate * grad_w_v
        values[b] -= learning_rate * grad_b_v

        print('%10d loss: %10.8f w1:%10.5f w2: %10.5f b: %10.5f'
              % (i, loss_v, values[w][0], values[w][1], values[b]))

        a = sess.run([y_pred], feed_dict=values)
        for i in range(4):
            print('%2d %2d %2d : %3.2f'
                  %(values[x][i][0], values[x][i][1], values[y][i][0], a[0][i]))

#출력이 2개가 되도록 구현하기
