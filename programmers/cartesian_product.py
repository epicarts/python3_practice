'''
변수들을 서로 곱하기 .
곱집합
'''


import itertools
a = 'ABCD'
b = 'xy'
c = '1234'

for i in a:
    for j in b:
        for k in c:
            print(i+j+k)
list(itertools.product(a,b,c))
[k for k in itertools.product(a,b,c)]

z
q
o
