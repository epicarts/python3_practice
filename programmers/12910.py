'''
나누어 떨어지느 숫자 배열
https://programmers.co.kr/learn/courses/30/lessons/12910

'''
from itertools import compress
list(compress(a,z))
compress
arr = [5, 9, 7, 10]
divisor = 5
z = tuple(map(divmod,arr,[divisor]*len(arr)))
a = [i[1] == 0 for i in z]
result = list(__import__("itertools").compress(arr,a))
a
arr
result.sort()


def solution(arr, divisor):
    answer = sorted(list(__import__("itertools").compress(arr,[i[1] == 0 for i in tuple(map(divmod,arr,[divisor]*len(arr)))])))
    return answer if len(answer) != 0 else [-1]

def solution(arr, divisor):
    arr = [x for x in arr if x % divisor == 0];
    arr.sort();
    return arr if len(arr) != 0 else [-1];
a
