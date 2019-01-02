'''
None에 특별한 의미를 부여시키는것은
None 이나 0 이나 빈문자열 이 조건식에서 Flase 로 평가된다.
None 를 반환하는 것 보다는 예외를 일으키자!!
'''
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

x = 0
y = 1
result = divide(x, y)
result
type(result)

#아래 if문은 None에 의미가 있을때 잘못된 예시임.
if not result:
    print('Invalid inputs')


'''
1. 반환값을 두개로 나눠서 튜플에 담는다.
별루다. 호출자가 튜플의 첫번쨰 부분을 쉽게 무시할 수 있다.
'''
def divide(a, b):
    try:
        return True, a / b
    except ZeroDivisionError:
        return False, None

sucess, result = divide(x, y)
if not sucess:
    print('Invalid inputs')

'''
2. 절대로 None을 반환하지 않는다.
호출 하는 쪽에 예외를 일으킨다. (입력값이 잘못됐음을 알린다)
'''
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError('Invalid inputs') from e

x, y = 1, 0
try:
    result = divide(x, y)
except ValueError:
    print('Invalid inputs')
else:
    print('Result is %.1f' % result)
