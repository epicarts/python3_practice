from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os


'''
read_csv
read_table
read_fwf
read_clipboard
'''
path = 'D:\\github\\python3_practice\\data_analysis\\datasets\\examples\\'
df = pd.read_csv(path+'ex1.csv')
df
pd.read_table(path,sep=',')
!type path+'ex2.csv'
pd.read_csv(path+'ex2.csv', header=None)#컬럼 부분을 생성 ㄴㄴ
pd.read_csv(path+'ex2.csv', names=['a', 'b', 'c', 'd', 'message'])#직접 칼럼지정
names = ['a', 'b', 'c', 'd', 'message']
pd.read_csv(path+'ex2.csv', names=names, index_col='message')
parsed = pd.read_csv(path+'csv_mindex.csv')

parsed = pd.read_csv(path+'csv_mindex.csv', index_col=['key1', 'key2'])
parsed
list(open(path+'ex3.txt'))
result = pd.read_table(path+'ex3.txt', sep='\s+') # 정규표현식 \s+ 사용.
result
a = open(path+'ex4.csv')
a.readlines()
pd.read_csv(path+'ex4.csv', skiprows=[0, 2, 3]) #row 건너 뛰기
result = pd.read_csv(path+'ex5.csv')
result
pd.isnull(result)#열었더니 누락된 값이 있음.
result = pd.read_csv(path+'ex5.csv', na_values=['NULL'])
result
sentinels = {'message': ['foo', 'NA'], 'something': ['two']}
sentinels
pd.read_csv(path+'ex5.csv', na_values=sentinels)

result = pd.read_csv(path+'ex6.csv')
pd.read_csv(path+'ex6.csv', nrows=3)#3줄만 읽음
chunker = pd.read_csv(path+'ex6.csv', chunksize=1000)#
chunker
tot = pd.Series([])
for piece in chunker:
    tot = tot.add(piece['key'].value_counts(), fill_value=0)
tot = tot.sort_values(ascending=False)#숫자 큰거부터 정렬
tot
result.head()
result.describe()

data = pd.read_csv(path+'ex5.csv')
data.to_csv(path+'out.csv')

import sys
data.to_csv(sys.stdout, sep='|')
data.to_csv(sys.stdout, na_rep='NULL')
data.to_csv(sys.stdout, index=False, header=False)
data.to_csv(sys.stdout, index=False)
import csv
class my_dialect((csv.Dialect)):
    lineterminator = '\n'
    delimiter = ';'
    quitercgar = '"'
    quoting = csv.QUOTE_MINIMAL

reader = csv.reader(f, dialect=my_dialect)

obj = """{"name": "Wes", "places_lived": ["United States", "spain", "Germay"], "pet": null, "siblings": [{"name": "Scott", "age": 25, "pet": "Zuko"}, {"name": "Katie", "age": 33, "pet": "Cisco"}]}"""
obj
import json
result = json.loads(obj) #JSON 문자열 =>  파이썬 형태로 변환
result#파이썬 형태
asjson = json.dumps(result)#파이썬 객체를 => JSON 형태로 변환.
asjson#json 형태
siblings = pd.DataFrame(result['siblings'], columns=['name','age'])
siblings
result['siblings']

import requests

from lxml.html import parse
from io import StringIO


test= requests.get('https://finance.yahoo.com/quote/AAPL/options?p=AAPL').text
parsed = parse(StringIO(test))
doc = parsed.getroot()
doc#HTML 태그가 추출되어 있음. table 태그도 있음.
#HTML 문서의 최상위에서 findall 메서드에 XPath 을 넘겨서
links = doc.findall('td')#.//a 가 들어간 엘리먼트를 모두 찾음 <.//a>
links[15:20]

#각 엘리먼트에 대해 get 메서드를 호출하려 URL으 얻어야함.
#get_content 메서드를 이용해서 링크 이름을 가져와야함.
lnk = links[28]
lnk.get('href')
lnk.text_content()


from lxml import objectify

parsed = objectify.parse(open(path+))

tag = '<a href="http://www.google.com">Google</a>'
root = objectify.parse(StringIO(tag)).getroot()
root
root.get('href')
root.text

'''
2진 데이터 형식
'''
frame = pd.read_csv(path+'ex1.csv')
frame#pickle 직렬화를 통해 데이터를 이진 형식으로저장하는 것.
frame
frame.to_pickle(path+'frame_pickle')

xls_file = pd.ExcelFile(path+'train.xls')
xls_file
pd.read_excel(open(path+'train.xls', 'rb'))


'''
API 이용
'''
import requests

url = 'https://api.github.com/repos/pydata/pandas/milestones/28/lables'
resp = requests.get(url)
resp
data = resp.json()
data
issue_labels = pd.DataFrame(data)
