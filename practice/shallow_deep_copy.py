'''
mutable(변하기 쉬운) 객체 가 있음
immutable(불변의) 객체 가 있음

list = mutable
set = mutable
str = immutable

'''


a = [1,2,3]#a리스트 생성
id(a)

#0번째 리스트 값에 상수를 변경해도 id 값은 변환 없음
a[0] = 5
id(a)

#set 함수를  합쳐도 id 값은 변환 없음
x = {1, 2, 3}
x
id(x)
x |= {4, 5, 6}
x
id(x)

#str은 immutable 이다.
#s 변수에 첫번째 글자를 변경 시도 하면 에러 발생
s = "abc"
id(s)
s[0]
s[0] = 'z'#에러 발생

#이건 재할당 문제임. mutable 하고는 다른문제.
# list 및 set도 재할당 시에 id 가 변경됨.
s = 'def'
id(s)
