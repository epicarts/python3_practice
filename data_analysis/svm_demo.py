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
'''
scale(X): 기본 스케일. 평균과 표준편차 사용
robust_scale(X): 중앙값(median)과 IQR(interquartile range) 사용. 아웃라이어의 영향을 최소화
minmax_scale(X): 최대/최소값이 각각 1, 0이 되도록 스케일링
maxabs_scale(X): 최대절대값과 0이 각각 1, 0이 되도록 스케일링
'''
x.min()
x.max()

# 0 ~ 1 사이로 스케일링 함.
x = (x-x.min())/(x.max()-x.min())
x.min()
x.max()
x.mean()


C = 1.0  # SVM 정규화 파라미터
#linear로 나누어 보쟈
models = svm.SVC(kernel='linear', C=C)
models.fit(x, y)

fig, sub = plt.subplots()
plt.subplots_adjust(wspace=0.4, hspace=0.4)
X0, X1 = x[:, 0], x[:, 1]
xx, yy = make_meshgrid(X0, X1)
plot_contours(sub, models, xx, yy,
              cmap=plt.cm.coolwarm, alpha=0.8)
sub.scatter(X0, X1, c=y, cmap=plt.cm.coolwarm, s=20, edgecolors='k')
sub.set_xlim(-0.25, 1.25)
sub.set_ylim(-0.25, 1.25)
sub.set_xlabel('X')
sub.set_ylabel('Y')

plt.show()


C = 1.0
models = svm.SVC(kernel='poly', degree=3, C=C, gamma='auto')
models.fit(x, y)

fig, sub = plt.subplots()
plt.subplots_adjust(wspace=0.4, hspace=0.4)

X0, X1 = x[:, 0], x[:, 1]
xx, yy = make_meshgrid(X0, X1)

plot_contours(sub, models, xx, yy,
              cmap=plt.cm.coolwarm, alpha=0.8)
sub.scatter(X0, X1, c=y, cmap=plt.cm.coolwarm, s=20, edgecolors='k')
sub.set_xlim(-0.25, 1.25)
sub.set_ylim(-0.25, 1.25)
sub.set_xlabel('X')
sub.set_ylabel('Y')

plt.show()


# RBF
C = 1.0  # SVM regularization parameter
models = svm.SVC(kernel='rbf', gamma=0.7, C=C)
models.fit(x, y)

# title for the plots
titles = ('SVC with RBF kernel')

# Set-up 2x2 grid for plotting.
fig, sub = plt.subplots()
plt.subplots_adjust(wspace=0.4, hspace=0.4)

X0, X1 = x[:, 0], x[:, 1]
xx, yy = make_meshgrid(X0, X1)

plot_contours(sub, models, xx, yy,
              cmap=plt.cm.coolwarm, alpha=0.8)
sub.scatter(X0, X1, c=y, cmap=plt.cm.coolwarm, s=20, edgecolors='k')
sub.set_xlim(-0.25, 1.25)
sub.set_ylim(-0.25, 1.25)
sub.set_xlabel('X')
sub.set_ylabel('Y')
sub.set_title(titles)

plt.show()
