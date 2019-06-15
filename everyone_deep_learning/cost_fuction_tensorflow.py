import numpy as np
import tensorflow as tf

X = np.array([1, 2, 3])
Y = np.array([1, 2, 3])

def cost_func(W, X, Y):
    # 기울기 * x값
    h = X * Y

    return tf.reduce_mean(tf.square(h - Y))

cost_values= []
#W 값을 -3 ~ 5 개 15구 소수 셋쨰자리까지
for feed_W in np.linspace(-3, 5, num=15):
    curr_cost = cost_func(feed_W, X, Y)
    cost_values.append(curr_cost)
    print("{:10.3f}|{:10.5f}".format(feed_W, curr_cost) )
