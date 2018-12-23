'''
소스코드 출처
https://m.blog.naver.com/PostView.nhn?blogId=samsjang&logNo=220955881668&proxyReferer=https%3A%2F%2Fwww.google.co.kr%2F
'''
#임계값 = 0
#학습률 = 0.1
#0보다 크면 1 그렇지 않으면 -1
#가중치(W) = 0으로 초기화

#만약 다르다면 , w = w + n(y - y^)x
#가중치 값을 수정함.

import numpy as np
class Perceptron():
    def __init__(self, thresholds=0.0, eta=0.01, n_iter=10):
        self.thresholds = thresholds
        self.eta = eta
        self.n_iter = n_iter

    def fit(self, X, y):
        self.w_ = np.zeros(1+X.shape=[1])
        self.errors_ = []

        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(X, y):
                update = self.eta * (target-self.predict(xi))
                self.w_[1:] += update * xi
                self.w_[0] += update
                errors += int(update!=0.0)
            self.errors_.append(errors)
            print(self.w_)

        return self

#x1, x2 가 인풋 일때 y 값은 평면인가? 평면이라면 어떻게?
def test_fun(x1, x2):
    return x1*0.5 + x2*0.5 - 0.7

# 0.7이 bias 0보다 커야함
test_fun(0,0)
test_fun(0,1)
test_fun(1,0)
test_fun(1,1)
