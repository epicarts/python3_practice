'''
몫과 나머지 구하기
strip() 양쪽의 빈 공백 지우기
split(' ')  ' ' 을 기준으로 나누기
map(int, input() ) input 을 각각 int() 함수에 적용.

큰 숫자를 쓸때는 divmod 가 빠름
작은 숫자를 쓸 때는 // % 연산이 더 빠름.
'''

a, b = map(int, input().strip().split(' '))

#case1
print(a//b,a%b)

#case2
divmod(a,b) # (a//b, a%b) 형태의 튜플로 반환됨.
print(*divmod(a,b))# *을 이용해 unpacking 함



# link https://stackoverflow.com/questions/30079879/is-divmod-faster-than-using-the-and-operators
# 숫자가 클 수록 더 빠름. 아래는 예제
import timeit
timeit.timeit('divmod(n, d)', 'n, d = 42, 7')
timeit.timeit('n // d, n % d', 'n, d = 42, 7')
timeit.timeit('divmod(n, d)', 'n, d = 2**74207281 - 1, 26', number=1)
timeit.timeit('n // d, n % d', 'n, d = 2**74207281 - 1, 26', number=1)
