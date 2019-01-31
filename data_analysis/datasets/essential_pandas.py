import pandas as pd
from pandas import Series, DataFrame
import numpy as np


obj = Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
obj
obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'], fill_value=0)
obj2
obj3 = Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
obj3
obj3.reindex(range(6))
obj3.reindex(range(6), method='ffill')#bfill 뒤의 값으로 채워 넣는다
frame = DataFrame(np.arange(9).reshape((3, 3)), index=['a', 'c', 'd'],
                  columns=['Ohio', 'texas', 'California'])
frame
frame2 = frame.reindex(['a', 'b', 'c', 'd'])
frame2
states = ['Ohio', 'texas', 'California']
frame.reindex(index=['a', 'b', 'c', 'd'], method='ffill')

obj = Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
new_obj = obj.drop('c')
new_obj
data = DataFrame(np.arange(16).reshape((4, 4)),
                 index=['Ohio', 'Colorada', 'Utah', 'New York'],
                 columns=['one', 'two', 'three', 'four'])
data
data.drop(['Colorada', 'Ohio'])
data.drop('two',axis=1)
data.drop(['two', 'four'],axis=1)
obj = Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
obj
obj['b']
obj[1]
obj[2:4]
obj[['b', 'a', 'd']]
obj[[1, 3]]
obj[[1, 3]]
obj[obj < 2]
obj['b':'c'] = 5
obj
data
data['two']
data[['two', 'one']]

data[:2]
data[data['three'] > 5]
data <  5
data[data < 5] = 0
data
data.loc['Colorada', ['two', 'three']]#column , [row select]
data.loc['Colorada']
data.loc[['Colorada', 'Ohio'], ['two', 'three']]
data.iloc[2]
data.loc[:'Utah', 'two']#행 Utah 까지 / 열 => 'two'
data
data.ix[data.three > 5, :3]
data.three > 5
df1 = DataFrame(np.arange(9.).reshape((3, 3)), columns=list('bcd'),
                index=['Ohio', 'Texas', 'Colorado'])
df2 = DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'),
                index=['Utah', 'Ohio', 'Texas', 'Oregon'])
df1
df2
df1+df2
df1.add(df2, fill_value=0)
df2.add(df1, fill_value=0)
arr = np.arange(12.).reshape((3, 4))
arr
arr[0]
arr - arr[0]
frame = DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'),
                  index=['Utah', 'Ohio', 'Texas', 'Oregon'])
series = frame.iloc[0]
series
frame
frame + series
series2 = Series(range(3), index=['b', 'e', 'f'])
series2#이건 아무런 name 이 없음
frame + series2
series
type(frame['b'])
type(frame)
series3 = frame['d']
frame.sub(series3, axis=0)
frame
series3

frame = DataFrame(np.random.randn(4, 3), columns=list('bde'),
                  index=['Utah', 'Ohio', 'Texas', 'Oregon'])

frame
np.abs(frame)#절대값
f = lambda x: x.max() - x.min()
frame.apply(f)
obj = Series(range(4), index=['d', 'a', 'b', 'c'])
obj.sort_index()
frame = DataFrame(np.arange(8).reshape((2, 4)), index=['three', 'one'],
                  columns=['d', 'a', 'b', 'c'])
frame
frame.sort_index(axis=0)
frame.sort_index(axis=1, ascending=False)
frame.sort_index(axis=1)
obj = Series([4, 7, -3, 2])
obj
obj.sort_values()
obj = Series([4, np.nan, 7, np.nan, -3, 2])
obj
obj.sort_index()
obj.sort_values()
frame = DataFrame({'b': [4, 7, -3, 2], 'a': [0, 1, 0, 1]})
frame
frame.sort_values(by='b')#b의 값기준으로 정렬
frame.sort_index(axis=1).sort_values(by='b') #a, b 순서 정렬 => b의 값별로 정렬
frame.sort_values(by=['a', 'b'])
'''
min 같은 값을 가지는 그룹을 낮은 순위로
max 같은 값을 가지는 그룹을 높은 순위로
average 같은 값을 가지는 항목의 평균 값을 순위로(defalut)
first 데이터 내에서 위치에 따라 순위를 매김
'''
obj = Series([7, 0-5, 7, 4, 2, 0, 4])
obj.rank()#공통도 나타 날 수 있음
obj.rank(method='first')#데이터 상의 나타내는 순서
obj.rank(ascending=False, method='max')#내림차순 순위
frame.rank(axis=1)
frame
obj = Series(range(5), index=['a', 'a', 'b', 'b', 'c'])
obj
obj.index.is_unique
obj['a']#중복되면 Series 값
obj['c']#중복되지 않으면 스칼라값
df = DataFrame(np.random.randn(4, 3), index=['a', 'a', 'b', 'b'])
df
df.loc['b']
df = DataFrame([[1.4, np.nan], [7.1, -4.5], [np.nan, np.nan], [0.75, -1.3]], index=['a', 'b', 'c', 'd'], columns=['one', 'two'])
df
df.sum()
df.sum(axis=0)
df.sum(axis=1)
df.mean(axis=1, skipna=False)#na 포함하겠다.
df
df.describe()

df = DataFrame(np.random.normal(loc=0, scale= 0.01, size=(5,4)),
               index=['2014-07-07', '2014-07-08', '2014-07-09', '2014-07-10', '2014-07-11',],
               columns=['AAPL', 'GOOG', 'IBM', 'MSFT']
               )
df.index.name = 'Date'
df
df.MSFT.corr(df.IBM)
