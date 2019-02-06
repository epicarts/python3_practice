import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_circles
from sklearn import svm, metrics
%matplotlib inline

'''
https://www.kaggle.com/maxl11/svm-demo
'''

def make_meshgrid(x, y, h=.02):
    """Create a mesh of points to plot in

    Parameters
    ----------
    x: data to base x-axis meshgrid on
    y: data to base y-axis meshgrid on
    h: stepsize for meshgrid, optional

    Returns
    -------
    xx, yy : ndarray
    """
    x_min, x_max = x.min() - 1, x.max() + 1
    y_min, y_max = y.min() - 1, y.max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    return xx, yy

def plot_contours(ax, clf, xx, yy, **params):
    """Plot the decision boundaries for a classifier.

    Parameters
    ----------
    ax: matplotlib axes object
    clf: a classifier
    xx: meshgrid ndarray
    yy: meshgrid ndarray
    params: dictionary of params to pass to contourf, optional
    """
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    out = ax.contourf(xx, yy, Z, **params)
    return out

samples = 500
train_prop = 5.0

#사이킷런 데이터셋에서 가져옴
x,y = make_circles(n_samples=samples, noise=0.05, random_state=123)
x[:,0]
x[:,0]
df = pd.DataFrame(dict(x=x[:, 0], y=x[:, 1], label=y))
df
groups = df.groupby('label')
groups

fig, ax = plt.subplots()
ax.margins(0.05)  # Optional, just adds 5% padding to the autoscaling
for name, group in groups:#그룹별로 분해.
    ax.plot(group.x, group.y, marker='o', linestyle='', ms=6, label=name)
ax.legend()
plt.show()

x.min()
x.max()

# 0 ~ 1 사이로 스케일링 함.
x = (x-x.min())/(x.max()-x.min())
x.min()
x.max()
x.mean()


C = 1.0  # SVM 정규화 파라미터
models = svm.SVC(kernel='linear', C=C)
models.fit(x, y)

'''
정수를 담은 이차원 리스트, mylist 가 solution 함수의 파라미터로 주어집니다.
 solution 함수가 mylist 각 원소의 길이를 담은 리스트를 리턴하도록 코드를
작성해주세요.

input [[1], [2]] /[[1, 2], [3, 4], [5]]

output
 [1,1]
 [2,2,1]
'''
