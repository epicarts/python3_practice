import numpy as np


data = np.random.randn(2, 3)
data
data * 10
data.shape
data.dtype

arr1 = np.array([1, 23, 21, 1.2])
arr1
arr1.shape
arr1.dtype

np.zeros(5)
np.ones((5,2))
np.empty((3, 3, 2))
np.arange(12)

arr1 = np.array([1, 2, 3], dtype=np.float64)
arr2 = np.array([1, 2, 3], dtype=np.int)
c = arr1 + arr2
c.dtype

arr = np.array([[1, 2, 3],[4, 5, 6]])
arr
arr * arr
1 / arr
arr - arr
arr ** 0.5
arr = np.arange(1,15)
arr_slice = arr[5:8]
arr[5:8]
arr_slice[1] = 123125
arr_slice
arr
arr_slice[:] = 64
arr
arr2d = np.arange(1,10)
arr2d = np.reshape(arr2d, (3,-1))
arr2d

arr3d = np.arange(12).reshape(2,2,3)
arr3d
arr3d[0]

a = np.arange(9)
arr2d = np.array([[1,2,3], 4])

old_values = arr3d[0].copy()
arr3d[0] = 42
arr3d
arr3d[0] = old_values
arr3d[0][0]
arr[1:6]
arr2d[:2]
arr2d
arr2d[:2,1:3]

arr2d[1, :2]
arr2d[:, :1]
arr2d[:2, 1:] = 0
arr2d
names = np.array(['Bob', 'Joe', 'will', 'Bob', 'will', 'Joe', 'Bob'])
names
data = np.random.randn(7, 4) #랜덤으로 채워진 7행 4열 생성
data
names == 'Bob'
data[names == 'Bob']
#축의 길이와 동일한 길이를 가져야 한다.
data[names == 'Bob',2:]
(names == 'Bob')
(names == 'will')
mask = (names == 'Bob') | (names == 'will')
mask
data[mask]

data[data < 0] = 0
data
data[names != 'Joe'] = 7
data
arr = np.empty((8,4))
arr
for i in range(8):
    arr[i] = i
arr
arr[[4, 3, 0, 6, 5]]
arr = np.arange(32).reshape((8, 4))
arr
arr[[1, 5, 7, 2],[0, 3, 1, 2]]
arr[np.ix_([1, 5, 7, 2],[0, 3, 1, 2])]

arr = np.arange(15).reshape((3,-1))
arr
arr.T

arr = np.random.randn(6, 3)
np.dot(arr.T, arr)

arr = np.arange(16).reshape((2, 2, 4))
arr
arr.transpose((1, 0, 2))
arr.swapaxes(1, 2)

'''
ufunc(유니버셜 함수): ndarray 안에 있는 데이터 원소별로 연산을 수행하는 함수

'''
arr = np.arange(10)
arr
np.sqrt(arr)
np.exp(arr)
x = np.random.randn(8)
x
y = np.random.randn(8)
y
np.maximum(x, y)

arr = np.random.randn(7) * 5
arr
np.modf(arr)

points = np.arange(-5, 5, 0.01)
points.shape

xs, ys = np.meshgrid(points, points)
xs, ys
z = np.sqrt(xs ** 2 + ys ** 2)
z
import matplotlib.pyplot as plt


# 개신기하네
plt.imshow(z, cmap=plt.cm.gray); plt.colorbar()

xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
xarr
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
yarr
cond = np.array([True, False, True, True, False])
cond

result = [(x if c else y) for x, y, c in zip(xarr, yarr, cond)]
result
result = np.where(cond, xarr, yarr)
result

arr = np.random.randn(4, 4)
arr
np.where(arr > 0, 1, 0)

np.where(arr > 0, 1, arr)

arr.mean()
np.mean(arr)
arr.sum()

arr.mean(axis=1)
arr.std()
arr.var()
arr.cumsum()
arr

arr = np.random.randn(100)
(arr > 0).sum()#True 인 개수 반환
bools = np.array([False, False, True, True])
bools
bools.any()
bools.all()

arr = np.random.randn(8)
arr
arr.sort()
arr
arr = np.random.randn(5, 3)
arr
arr.sort(0)
arr

large_arr = np.random.randn(1000)
large_arr.sort()

large_arr[int(0.05 * len(large_arr))]


names = np.array(['Bob', 'Joe', 'will', 'Bob', 'will', 'Joe', 'Bob'])
np.unique(names)

ints = np.array([3, 3, 3, 2, 2, 1, 1, 1, 4, 4])
ints
np.unique(ints)

sorted(set(names))

values = np.array([6, 0, 0, 3, 2, 5, 6])
#2개의 배열을 인자로 받아, 첫번째 배열의 가 원소가 두번ㅋ째 배열의 원소를 포함하는지 확인
np.in1d(values, [2, 3, 6])

'''
파일 입출력
'''
arr = np.arange(10)
np.save('some_array', arr)

np.load('some_array.npy')

np.savez('array_archive.npy', a=arr, b=arr)

arch = np.load('array_archive.npy.npz')
arch['a']
arch['b']
arch.files

x = np.array([[1, 2, 3], [4, 5, 6]])
y = np.array([[6, 23], [-1, 7], [8, 9]])
np.dot(x,y)

np.dot(x, np.ones(3))

from numpy.linalg import inv, qr

X = np.random.randn(5, 5)
mat = X.T.dot(X)
X
mat
inv(mat)#X를 전치하고 X를 곱한 식.
np.dot(mat, inv(mat))
mat.dot(inv(mat))
q, r = qr(mat)
r

samples = np.random.normal(size=(4, 4))
samples
samples.std()
samples.mean()

from random import normalvariate

N = 1000000

%timeit samples = [normalvariate(0, 1) for _ in range(N)]

%timeit np.random.normal(size=N)

import random
position = 0
walk = [position]
steps = 1000
for i in range(steps):
    step = 1 if random.randint(0, 1) else - 1
    position += step
    walk.append(position)
import matplotlib.pyplot as plt
plt.plot(range(100),walk[:100])

nsteps = 1000
draws = np.random.randint(0, 2, size=nsteps)
steps = np.where(draws > 0, 1, -1)
walk = steps.cumsum()

walk.min()
walk.max()
(np.abs(walk) >= 10).argmax()

nwalks = 5000
nsteps = 1000
draws = np.random.randint(0, 2, size=(nwalks, nsteps))
draws.shape
steps = np.where(draws > 0, 1, -1)
walks = steps.cumsum(1)
walks
walks.max()
walks.min()
hits30 = (np.abs(walks) >= 30).any(1)
hits30
hits30.sum()

crossing_times = (np.abs(walks[hits30]) >= 30).argmax(1)
crossing_times.mean()
