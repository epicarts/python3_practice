import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pandas import DataFrame, Series

data = DataFrame({'X': [1, 2, 3, 4, 5], 'Y': [2.1, 3.1, 4.1, 5.1, 6.1]},dtype=np.float32)

tf.set_random_seed(777)  # for reproducibility
W = tf.Variable(tf.random_normal([1]), name="weight")
b = tf.Variable(tf.random_normal([1]), name="bias")

X = tf.placeholder(tf.float32, shape=[None])
Y = tf.placeholder(tf.float32, shape=[None])

hypothesis = X * W + b
cost = tf.reduce_mean(tf.square(hypothesis - Y))
train = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(2001):
    _, cost_val, W_val, b_val = sess.run(
        [train, cost, W, b], feed_dict={X: data.X, Y: data.Y})
sess.run(hypothesis)f
sess.run(cost_val)


with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for step in range(2001):
        _, cost_val, W_val, b_val = sess.run(
            [train, cost, W, b], feed_dict={X: data.X, Y: data.Y})
        if step % 20 == 0:
            print(step, cost_val, W_val, b_val)


'''
'''
X_place = tf.placeholder(tf.float32, shape=[None])
Y_place = tf.placeholder(tf.float32, shape=[None])

#tensorflow 에서 변하는 변수 정의
variable_random = tf.random_normal([1])
W = tf.Variable(variable_random, tf.float32, name='Weight')
b = tf.Variable(variable_random, tf.float32, name='bais')

#가설을 세워보자 y = ax + b 선형으로
hypothesis = X_place * W + b

#코스트 함수로 쓸만한건 ??
#결과값과 예측값의 차이로 하면 좋을듯 하다. 거리 공식으로 차이점을 알아내쟈
cost = tf.reduce_mean(tf.square(hypothesis - Y_place))

#조절은 어떻게 할 것인가 ? 경사하강법. 학습률은 ?
optimizer = tf.train.GradientDescentOptimizer(0.03, name='GD')

#학습은 무엇으로 할것인가?경사하강법. 코스트가 어떻게 되는 값을 학습이 된다고 할까? 최소
train = optimizer.minimize(cost)

#그래프를 만들었으니 실행을 해야된다. sess 하나를 만들어 준다.
with tf.Session() as sess:
    #Variable 를 run 하기 위해서는 초기화가 필요하다.
    sess.run(tf.global_variables_initializer())
    #본격적으로 학습을 해보자.
    for i in range(4001):
        sess.run(train, feed_dict={X_place: data.X, Y_place: data.Y})
        if i % 400 == 0:#400번 학습 시마다.
            plt.plot(data.X, data.Y, linestyle='', marker='o', markersize=12)
            plt.plot(data.X, sess.run(hypothesis))#line을 그려보자
            print("현재까지 손실율:",sess.run(cost))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for step in range(2001):
        _, cost_val, W_val, b_val = sess.run(
            [train, cost, W, b], feed_dict={X: data.X, Y: data.Y})
        if step % 20 == 0:
            print(step, cost_val, W_val, b_val)
