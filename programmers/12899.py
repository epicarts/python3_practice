'''

https://programmers.co.kr/learn/courses/30/lessons/12899

124 나라

'''
#3으로 나누됨


def solution(n):
    return convert(n - 1)

def convert(n):
    T = "124"
    a,b = divmod(n,3)
    if a == 0:
        return T[b]
    else:
        return convert(a-1) + T[b]
