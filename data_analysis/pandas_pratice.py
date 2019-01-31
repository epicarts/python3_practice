from pandas import Series, DataFrame
import pandas as pd
import numpy as np


obj = Series([4, 7, -5, 3])#왼쪽에 색인, 오른쪽은 색인의 값
obj

obj.values
obj.index

obj2 = Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
obj2
obj2['a']
obj2['d'] = 6
obj2
obj2[['c', 'a', 'd']]
obj2[obj2 > 0]
obj2 > 0
'b' in obj2

sdata = {'dfd': 2213, 'dsfsdf': 123123, '232fsad':123123}
obj3 = Series(sdata)
obj3
states = ['dfd', 'sdnflsdnf','flame', '232fsad']
obj4 = Series(sdata, index=states)
obj4
pd.isnull(obj4)
pd.notnull(obj4)
obj4.isnull()
obj3
obj4
obj3 + obj4

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'asd', 'asd'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = DataFrame(data)
frame
DataFrame(data, columns=['year', 'state', 'pop'])
data
frame2 = DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
                   index=['one', 'two', 'three', 'four', 'five'])
frame2
frame2['state']
frame2.year
frame2.loc['three']
frame2['debt'] = 16.5#컬럼 전부 대입
frame2
frame2['debt'] = np.arange(5)
frame2
frame2.columns
val = Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
val
frame2['debt'] = val
frame2

frame2['eastern'] = frame2.state == 'Ohio'
frame2

del frame2['eastern']
frame2
pop = {'asd': {2001: 2.4, 2002: 2.9},
       'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
frame3 = DataFrame(pop)
frame3.T
DataFrame(pop, index=[2001, 2002])
pop

frame3.index.name = 'year'; frame3.columns.name = 'state'
frame3
frame3.values
obj = Series(range(3), index=['a', 'b', 'c'])
obj
index = obj.index
index
index[1] = 'd' #인덱스 는 변경할 수 없다.

index = pd.Index(np.arange(3))#인덱스 객체 생성
index
obj2 = Series([1.5, -2.5, 0], index=index)# 자료구조 사이에서 수정해야함..
obj2
frame3
