from pandas import DataFrame, Series

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import json

path = 'datasets\\bitly_usagov\\example.txt'
records = [json.loads(line) for line in open(path, encoding='UTF8')]
records[0]
records[0]['tz']



time_zones = [rec['tz'] for rec in records if 'tz' in rec]
time_zones

df = DataFrame(records)
df.info()
df.describe()
df['tz'][:10]
tz_count = df['tz'].value_counts()
tz_count
clean_tz = df['tz'].fillna('Missing')#비어 있는 값을 대체
clean_tz[clean_tz == ''] = 'Unknown'
clean_tz.value_counts()
#top 10 개에 대해 bar 형태로 그림을 그림.
tz_count[:10].plot(kind='barh', rot=0)
#단말기 application 정보를 담은 필드
df['a'][1]
df['a'][50]
results = Series([x.split()[0] for x in df.a.dropna()])#df의 a속성에 na 값들을 drop 시킴
df.shape
results.shape
results.head()
results.value_counts()[:10]
'''
윈도우 사용자와 비 윈도우 사용자 그룹으로 나누어 보자
'''

cdf = df[df.a.notnull()]#agent값이 없는 데이터를 제외

#cdf의 a 속성에 Windows 가 포함되면 Ture / False 로 나눔.
#np.where: True: Windows 라고 표시, False: Not windows 라고 표시
op_system = np.where(cdf['a'].str.contains('Windows'), 'Windows', 'Not windows')
cdf['a'].str.contains('Windows')
op_system
by_tz_os = cdf.groupby(['tz', op_system])#운영체제 그룹과 'tz'를 합침
agg_counts = by_tz_os.size().unstack().fillna(0)#unstack함수를 이용하여 표로 배치
indexer = agg_counts.sum(1).argsort()
agg_counts[:10]
indexer[:10]
count_subset = agg_counts.take(indexer)[-10:]
count_subset
count_subset.plot(kind='barh', stacked=True)

#정규화
normed_subset = count_subset.div(count_subset.sum(1), axis = 0)
normed_subset.plot(kind='barh', stacked=True)
count_subset.sum(1)
count_subset
normed_subset
