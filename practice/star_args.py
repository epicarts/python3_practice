'''
선택적인 위치 인수 *args = star args

'''

def log(message, values):
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print('%s: %s' % (message, values_str))

log('My numbers are', [1, 2])
log('Hi there', [])#로그로 남길 값이 없을때 빈리스트를 넘겨야 하는건 불-편함

def log2(message, *values):
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print('%s: %s' % (message, values_str))

log2('My numbers are', 1, 2)
log2('Hi there')#로그로 남길 값이 없을때 빈리스트를 넘겨야 하는건 불-편함

favorites = [7, 33, 99]
#가변인수가 함수에 전달되기에 앞서 항상 튜플로 변환됨
#함수를 호출하는 쪽에서 제너리에터에 *을 쓰면 제너레이터가 모두 소진될떄까지 순회됨.
#메모리를 많이 차지함
log2('flksdnfklsdnf', *favorites)


def my_generator():# 0~ 10까지 생성하는 제너레이터 만듬
    for i in range(10):
        yield i

def my_func(*args):
    print(args)

it = my_generator()
my_func(*it)
my_func(*[1,2,3,4,5,6])
