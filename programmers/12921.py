'''
소수 찾기
https://programmers.co.kr/learn/courses/30/lessons/12921
'''

def solution(n):
    n_list = list(range(2,n+1))
    for i in range(int(n**(0.5))):
        n_list = [n for n in n_list if n is n_list[i] or n % n_list[i] is not 0]
    return len(n_list)

def sieve(n):
    """Return list of prime numbers less than equal to n"""

    results = [1 for _ in range(n+1)]
    results[0], results[1] = 0, 0
    results = [0,0] + [1]*(n - 1)
    len(results)
    div = 2

    for i,num in enumerate(results):
        if num:
            k = i * 2
            while k <= n:
                seive[k] = 0
                k+= i
    return [x for (x,y) in enumerate(results) if y]

    while div <= n // 2 + 1:
        for i in range(div * div, n+1, div):
            if results[i] == 0:
                continue
            else:
                results[i] = 0
        div += 1

    #return sum(results)
    return [i for i in range(len(results)) if results[i] == 1]
solution(1000000)
sieve(1000000)
n=10000
