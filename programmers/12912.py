'''
https://programmers.co.kr/learn/courses/30/lessons/12912
두 정수 사이의 합
두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의
합을 리턴하는 함수
'''

a = 3
b = 5
a,b

[sum(i) for i in range(b ) + ]
list(range(a, b + 1, 1))
sum(list(range(min(a,b),max(a,b)+1, 1)))

def solution(a, b):
    return sum(list(range(min(a,b),max(a,b)+1, 1)))
