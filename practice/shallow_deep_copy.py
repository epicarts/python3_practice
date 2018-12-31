'''
mutable(변하기 쉬운) 객체 가 있음
immutable(불변의) 객체 가 있음

list = mutable
set = mutable
str = immutable

1. mutable(list, set) 은 변수 대입을 하면 값도 같이 변함. 주소가 안바뀜
2. immutable(str)은 변수 대입을 하면 재할당이되서 주소가 바뀜
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

#mutable 객체의 변수 간의 대입
#값이 할당 되는것이 아니라 같은 메모리 주소를 공유함(포인터???)
#b를 변경하면 a도 바뀜
a = [1, 2, 3]
b = a
b[0] = 4
id(a)
id(b)
a
b


#immutable 객체 변수 간의 대입
#str을 사용함. 재할당을 하게됨.
a = "abc"
b = a
a
b
id(a)
id(b)
b = "abcde"
a
b
id(a)
id(b)

#얕은 복사 (shallow copy)
a = [[1,2], [3,4]]
#슬라이싱을 이용하면,
b = a[:]
id(a)
id(b)
#서로 영향을 받지 않음.
id(a[0])
id(b[0])
#그러나 내부의 값은 같은 주소를 바라보고있음.

a[0] = [8,9]
id(a[0])
id(b[0])
#재할당 할 경우 메모리 주소도 달라짐

a[1].append(5)
a
b
#그러나 a[1]의 값을 변경하면 안에 있는 값도 변경됨.
#리스트 주소 자체는 다르지만, 안에 있는 원소들의 주소는 공유하기 떄문

#깊은 복사(deep copy)
#내부에 객체들까지 새롭게 copy 됨
import copy
a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)
a[1].append(5)
a
b
