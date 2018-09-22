'''
순열과 조합!!!
엄청 돌ㅇ갔던거
combinations, permutations
카카오 사진찍기 예시

range(시작, 끝, 증가값)
range(시작, 끝)
range(끝)

'''
#https://programmers.co.kr/learn/courses/4008/lessons/12836
def permutation(iterable, n, r):
    if r == 0:
        print(iterable)
        print("end r == 0 ")
        return
    for i in range(n-1, -1, -1):
        iterable[i], iterable[i-1] = iterable[i-1], iterable[i]
        permutation(iterable, n-1, r-1)
        iterable[i], iterable[i-1] = iterable[i-1], iterable[i]

pool = ['A', 'B', 'C']
permutation(pool, len(pool), len(pool))
list(range(2,-1,-1))


import itertools

pool = ['A', 'B', 'C']
print(list(map(''.join, itertools.permutations(pool)))) # 3개의 원소로 수열 만들기
print(list(map(''.join, itertools.permutations(pool, 2)))) # 2개의 원소로 수열 만들기
help()
