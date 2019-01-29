import numpy as np
import pandas as pd
import os

'''
1990 ~ 2000년대까지 사용자들로부터 수집한 영화 평점 데이터
영화평점, 영화 정보, 사용자에 대한 정보.
'''

encoding = 'latin1'
upath = os.path.expanduser('datasets\\movielens\\users.dat')
rpath = os.path.expanduser('datasets\\movielens\\ratings.dat')
mpath = os.path.expanduser('datasets\\movielens\\movies.dat')

unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
mnames = ['movie_id', 'title', 'genres']

users = pd.read_csv(upath, sep='::', header=None, names=unames, encoding=encoding)
ratings = pd.read_csv(rpath, sep='::', header=None, names=rnames, encoding=encoding)
movies = pd.read_csv(mpath, sep='::', header=None, names=mnames, encoding=encoding)

users.head()
ratings.head()
movies.head()

#나이 + 성별에 따른 영화 평점
a = pd.merge(ratings, users)
data = pd.merge(a, movies)
data.head()
a.info()
movies.head()
ratings.head()
users.head()
pd.merge(ratings, users)
data.loc[0]#각 유저별 영화 장르별 평점 정보를 수집
#비율. index는 제목, columns 은 성별, agg함수는 평균.
mean_ratings = data.pivot_table('rating', index='title', columns='gender',
                                aggfunc='mean')
mean_ratings.head()
ratings_by_title = data.groupby('title').size()
#데이터를 title에 의해서 그룹화 시킴
ratings_by_title # type = Series
active_titles = ratings_by_title.index[ratings_by_title >= 250]
active_titles#ratings_by_title의 컬럼에서 250 이상인 인덱스만 뽑아냄
type(active_titles)
mean_ratings = mean_ratings.ix[active_titles]
top_female_ratings= mean_ratings.sort_index(by='F', ascending=False)
top_female_ratings
mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']#기존 열 추가 시키기도 가능함.
sorted_by_diff = mean_ratings.sort_values(by='diff')
sorted_by_diff[::-1][:15]
#호불호가 극명하게 나뉘는 영화찾기 = 평점의 분산이나 표준편차를 통해 측정 가능
ratings_by_title = data.groupby('title')['rating'].std()
rating_std_by_title = ratings_by_title.ix[active_titles]
rating_std_by_title.sort_values(ascending=False)[:10]
