'''
파이썬 루프에서는 루프에서 반복되는 내부블록 바로다음에 else를 쓸 수 있다!
for 문을 다 돌고나면 else 문이 자동으로 실행된다.(if else와는 다른 개념.)
break를 사용하면 else 문이 생략 된다
별로 추천하지는 않는다.
'''
#파이썬 루프가 끝나고 else 가 실행됨
for i in range(3):
    print('Loop %d' % i)
else:
    print('Else block!')

# break를 쓰면 else는 생략된다.
for i in range(3):
    print('Loop %d' % i)
    if i == 1:
        break
else:
    print('Else block!')
#시퀀스가 비어 있지만 else 블록이 즉시 실행됨
for x in []:
    print('never runs')
else:
    print('for else block!')

#물론 while False 일 경우에도 실행됨
while False:
    print('never runs')
else:
    print('for else block!')

#서로소 인지 판별할때 사용해보자
a = 4
b = 9
for i in range(2, min(a, b) + 1):
    print('test', i)
    #둘다 나눳을때 0이 나와야함
    if a % i == 0 and b % i == 0:
        print('Not coprime')
        break
else:#for 문의 else 이다
    print('coprime')

#위에 else 쓰는 것 보다는 helper function이 나음
def coprime(a, b):
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            return False
    return True
