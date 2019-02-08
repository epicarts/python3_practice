import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pandas import DataFrame, Series

#분석할 데이터 셋
data = DataFrame({'X': [1., 2., 3., 4., 5.], 'Y': [2.1, 3.1, 4.1, 5.1, 6.1]},dtype=np.float32)
data

#데이터에 대해 시각화를 해보자 (상관 관계파악)
#딱봐도 y=ax + 관계이다.
plt.plot(data.X, data.Y, linestyle='', marker='o', markersize=12)

#placeholder 정의
#input: 내가 넣을 데이터 셋,
#반드시 run 할때 feed_dict 값을 넣어 줘야한다. feed_dict={X: data.X, Y: data.Y}
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
#cost = tf.sqrt(tf.reduce_mean(tf.square(hypothesis - Y_place)))



#조절은 어떻게 할 것인가 ? 경사하강법. 학습률은 ?
optimizer = tf.train.GradientDescentOptimizer(0.01, name='GD')

#학습은 무엇으로 할것인가?경사하강법. 코스트가 어떻게 되는 값을 학습이 된다고 할까? 최소
train = optimizer.minimize(cost)

plt.figure(figsize=[16, 8])
ax1 = plt.subplot(121)
ax2 = plt.subplot(122)

#그래프를 만들었으니 실행을 해야된다. sess 하나를 만들어 준다.
with tf.Session() as sess:
    #Variable 를 run 하기 위해서는 초기화가 필요하다.
    sess.run(tf.global_variables_initializer())
    #본격적으로 학습을 해보자.
    for i in range(700):
        #W, cost, _ = sess.run([Weight, cost, train], feed_dict={X_place: data.X, Y_place: data.Y})
        cost_val, W_val, b_val, _ = sess.run([cost, W, b, train], feed_dict={X_place: data.X, Y_place: data.Y})
        if i % 3 == 0:#400번 학습 시마다.
            ax1.plot(data.X, data.Y, linestyle='', marker='o', markersize=12)
            ax1.plot(data.X, data.X*sess.run(W)+sess.run(b))#line을 그려보자
            ax1.set_xlabel('X Data')
            ax2.set_ylabel('Y Data')

            ax2.plot(W_val, cost_val, marker='x', markersize=12)#line을 그려보자
            ax2.set_xlabel('Weight value')
            ax2.set_ylabel('cost value')
            print("cost: ",cost_val, " bais: ",b_val," weight: ",W_val)
    #학습이 끝나면 저장
    writer = tf.summary.FileWriter("./testgraph")
    writer.add_graph(sess.graph)
plt.show()
