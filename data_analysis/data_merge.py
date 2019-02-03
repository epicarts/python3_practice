from pandas import Series, DataFrame
import pandas as pd
import numpy as np


df1 = DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                 'data1': range(7)})
df2 = DataFrame({'key': ['a', 'b', 'c'],
                 'data2': range(3)})
df1
df2
pd.merge(df1, df2)#겹치는 칼럼인 key를 키로 선택하여 합친다.
pd.merge(df1, df2, on='key')#이런 습관을 들이는게 좋음
df3 = DataFrame({'key1': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                 'data1': range(7)})
df4 = DataFrame({'rkey': ['a', 'b', 'c'],
                 'data2': range(3)})
pd.merge(df3, df4, left_on='key1', right_on='rkey')#df3는 key1기준,df4는 rkey 기준
df3
df4
pd.merge(df1, df2, how='right')
df1 = DataFrame({'key': ['b', 'b', 'a', 'c', 'a' ,'b'],
                 'data1': range(6)})
df2 = DataFrame({'key': ['a', 'b', 'a', 'b', 'd'],
                 'data2': range(5)})
df1
df2
pd.merge(df1, df2, on='key', how='right')#df2에 있는 키를 기준으로 df2의 모든 경우의 수

pd.merge(df1, df2, on='key', how='left')#df1에 있는 키를 기준으로 df2의 모든 경우의 수
pd.merge(df1, df2, how='inner')
left = DataFrame({'key1': ['foo', 'foo', 'bar'],
                  'key2': ['one', 'two', 'one'],
                  'lval': [1, 2, 3]})
right = DataFrame({'key1': ['foo', 'foo', 'bar', 'bar'],
                   'key2': ['one', 'one', 'one', 'two'],
                   'lval': [4, 5, 6, 7]})
left
right
pd.merge(left, right, on=['key1', 'key2'], how='outer')
pd.merge(left, right, on=['key1', 'key2'], how='inner')
pd.merge(left, right, on=['key1', 'key2'], how='left')

left1 = DataFrame({'key': ['a', 'b', 'a', 'a', 'b', 'c'],
                   'value': range(6)})
right1 = DataFrame({'group_val': [3.5, 7]}, index=['a', 'b'])
left1
right1
pd.merge(left1, right1, left_on='key', right_index=True)#왼쪽은 key 오른쪽은 index
lefth = DataFrame({'key1': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
                   'key2': [2000, 2001, 2002, 2001, 2002],
                   'data': np.arange(5.)})
righth = DataFrame(np.arange(12).reshape((6,2)),
                   index=[['Nevada', 'Nevada', 'Ohio', 'Ohio', 'Ohio', 'Ohio'],
                          [2001, 2000, 2000, 2000, 2001, 2002]],
                   columns=['event1' , 'event2'])

lefth
righth
pd.merge(lefth, righth, left_on=['key1', 'key2'], right_index=True)

left2 = DataFrame([[1, 2], [3, 4], [5, 6]], index=['a', 'c', 'e'],
                  columns=['Ohio', 'Nevada'])
right2 = DataFrame([[7, 8], [9, 10], [11, 12], [13, 14]],
                   index=['b', 'c', 'd', 'e'], columns=['Missouri', 'Alabma'])
right2
left2
pd.merge(left2, right2, how='outer', left_index=True, right_index=True)
left2.join(right2, how='outer')#join 메서드는 칼럼이 켭치지 않고 완전히 같거나 유사한 색인구조 통합
left1.join(right1, on='key')
another = DataFrame([[7, 8], [9, 10], [11, 12], [16, 17]],
                    index=['a', 'c', 'e', 'f'],
                    columns=['New York', 'Oregon'])
another
left2.join([right2, another])
right2
left2
left2.join([right2, another], how='outer')
'''
합치기전에 고려해야 할 사항
1. 만약 연결하려는 두객체의 색인이 서로 다르다면, 교집합? 합집합 ?
2. 합쳐진 결과에서 합쳐지기전 객체의 데이터를 고려할 수 있음 ?
3. 어떤 축으로 연결할거임?
'''

arr = np.arange(12).reshape((3,4))
arr
np.concatenate([arr, arr], axis=1)
s1 = Series([0, 1], index=['a', 'b'])
s2 = Series([2, 3, 4], index=['c', 'd', 'e'])
s3 = Series([5, 6], index=['f', 'g'])
pd.concat([s1, s2, s3])
pd.concat([s1, s2, s3], axis=1) #행axis=0  열axis=1 을 통합.

s4 = pd.concat([s1 * 5, s3])
pd.concat([s1, s4], axis=1)
pd.concat([s1, s4], axis=1, join='inner')

#인자로 하려는 축을 직접 지정 할 수 있다.
pd.concat([s1, s4], axis=1, join_axes=[['a', 'c', 'b', 'e']])
result = pd.concat([s1, s1, s3], keys=['one', 'two', 'three'])
result
result.unstack()
result = pd.concat([s1, s1, s3], axis=1, keys=['one', 'two', 'three'])
result
df1 = DataFrame(np.arange(6).reshape(3, 2), index=['a', 'b', 'c'],
                columns=['one', 'two'])

df2 = DataFrame(np.arange(4).reshape(2, 2), index=['a', 'c'],
                columns=['three', 'four'])
df1
df2
pd.concat([df1, df2], axis=1, keys=['level1', 'level2'])
pd.concat({'level1': df1, 'level2': df2}, axis=1)
pd.concat([df1, df2], axis=1, keys=['level1', 'level2'],
          names=['upper', 'lower'])
df1

#DataFrmae의 로우 색인이 분석에 불필요한 경우
df1 = DataFrame(np.random.randn(3, 4), columns=['a', 'b', 'c', 'd'])
df2 = DataFrame(np.random.randn(2, 3), columns=['b', 'd', 'a'])
df1
df2
pd.concat([df1, df2], ignore_index=True)
a = Series([np.nan, 2.5, np.nan, 3.5, 4.5, np.nan],
           index=['f', 'e', 'd', 'c', 'd', 'a'])
b = Series(np.arange(len(a), dtype=np.float64),
           index=['f', 'e', 'd', 'c', 'b', 'a'])
a
b[-1] = np.nan
b
np.where(pd.isnull(a), b, a)#3항연산자
pd.isnull(a)
np.where
b

'''
피벗
표 형식의 데이터를 재배치하는 다양한 기본 연산. 재형성 또는 피벗 연산이라고함
'''
data = DataFrame(np.arange(6).reshape((2, 3)),
                 index=pd.Index(['Ohio', 'Colorado'], name='state'),
                 columns=pd.Index(['one', 'two', 'three'], name='number'))
data
result = data.stack()#칼럼이 로우로 피벗됨.
result
result.unstack()#계층적 색인을 가진 Series로부터 DataFrame을 얻음
result.unstack(0)#방향을 바꿈
result.unstack('state')#이름 => 컬럼
s1= Series([0, 1, 2, 3], index=['a', 'b', 'c', 'd'])
s1
s2 = Series([4, 5, 6], index=['c', 'd', 'e'])
s2
data2 = pd.concat([s1, s2], keys=['one', 'two'])
data2
data2.unstack(1)
data2.unstack().stack(dropna=False)
df = DataFrame({'left': result, 'right': result + 5},
               columns=pd.Index(['left', 'right'], name='side'))
df
df.unstack('state')
df.unstack('state').stack('side')
path = 'D:\\github\\python3_practice\\data_analysis\\datasets\\examples\\'
data = pd.read_csv(path+'macrodata.csv')
data.head()
periods = pd.PeriodIndex(year=data.year, quarter=data.quarter, name='data')
periods
