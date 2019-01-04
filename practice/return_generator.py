'''
함수 리턴값 => 리스트(간단한 방법)

ex) 문자열에 있는 모든 단어의 인덱스를 출력

잠깐!
Iterator = next 메서드를 가지고 있는 객체.
순차적으로 원소들을 탐색, 메서드 호출시마다 새로운 객체를 반환함.

generator = iterable 이면서 iterator 인 객체의 특별 종류
별도의 리스트로 저장을 하지 않으므로 메모리를 절약 할 수 있다.
다양한 입력(입력이 많아도) 쉽게 이용 할 수 있다.

제너레이터를 정의할떄 알아둬야 하는것
이터레이터에 상태가 있고 재사용할 수 없다는 사실을 호출하는 쪽에서 알아야 함

yield : 함수 실행 중간에 빠져나올수 있는 generator 를 만들 때 사용함.
'''

#두가지 문제점이 있다.
#1. 코드가 복잡하고 깔끔하지 않다.
#2. 결과 리스트를 생성하는데 한줄, 반환하는데 한
def index_words(text):
    result = []
    if text:#만약 텍스트가 있다면
        result.append(0)
        for index, letter in enumerate(text):
            if letter == ' ':#띄어쓰기가 나올때마다
                result.append(index + 1)#배열의 위치를 표시함
        return result

address = 'Four score and seven years ago...'
result = index_words(address)
result

#제너레이터를 사용해보자(generator)
#제너레이터는 yield 표현식을 사용하는 함수이다
#next를 호출할떄마다 이터레이터는 제너레이터가 다음 yield 표현식으로 진행

def index_words_iter(text):
    if text:
        yield 0#결과값은 list 형식이 아닌 yield 표현식으로 전달됨.
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1

result = list(index_words_iter(address))
result

index_generator = index_words_iter(address)
next(index_generator)
next(send.index_generator)
index_generator.send(2)

#yield 가 나올 때 마다 제너레이터 멈춤
def index_file(handle):
    offset = 0
    for line in handle:# 라인 한 줄씩 읽어옴
        if line:
            yield offset#라인이 있다면 0 출력
        for letter in line:#라인에 단어 한줄씩 가져옴
            offset += 1#offset 값을 하나 늘림
            if letter == ' '#빈칸이 나온다면
                yield offset#그때 한줄 출력.

#같은 결과가 나옴
with open('text.txt', 'r') as f:
    it = index_file(f)
    results = islice(it, 0, 3)
    print(list(results))


a = range(10)
a
c = iter(a)
c.send(2)

def gen():
    for i in range(10):
        yield i ** 3

for x in gen():
    print(x)
a = gen()
next(a)
def gen():
    yield 'one'
    yield 'two'
    yield 'three'
