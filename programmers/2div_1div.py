'''
2차원 리스트를 1차원 리스트로 만들기
'''
list1 = [[1], [2]]
list2 = [['A', 'B'], ['X', 'Y'], ['1']]
list3 = [['A', 'B'], [['A', 'B'],'X', 'Y'], ['1']]


sum(list1,[])
sum(list2,list1)

import itertools
a =list(itertools.chain.from_iterable(list3))
list(itertools.chain.from_iterable(a))
