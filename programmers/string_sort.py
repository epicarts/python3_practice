'''
ljust 좌측 정렬
center 가운데정렬
rjust 우측 정렬

'''
s, n = input().strip().split(' ')
n = int(n)
s.ljust(n)
s.center(n)
s.rjust(n)



'''
원본을 유지한채 정렬된 리스트 구하기
'''

list1 = [3, 2, 1]
list2 = [i for i in list1] # 또는 copy.deepcopy를 사용
list2.sort()
list2

list2 = sorted(list1)
list2
a = list (reversed(list2))
a
