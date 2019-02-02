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
lefth
DataFrame()
pd.merge()
!tpye "sdf"
