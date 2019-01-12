'''
API 는 후크를 이용하여 작성한 코드를 실행 중에 호출.

함수가 후크로 동작하는 이유는 파이썬이 일급함수(first-class function)
즉, 함수와 메서드를 다른값처럼 전달하고 참조할 수 있기 떄문
'''

names = ['Socrates', 'Archimedes', 'Plato', 'Aristotle']
#람다 표현식을 key후크로 넘겨서 이름의 리스트를 길이로 정렬
names.sort(key =lambda x: len(x))
names

current = {'green': 12, 'blue': 3}

increments = [('red', 5), ('blue', 17), ('orange', 9)]



#call 이라는 메서드는 객체를 함수처럼 호출할 수 있게 해줌.
#__call__ 메서드는 클래스의 인스턴스를 일반 파이썬 함수 처럼 호출 할 수 있게 해줌.
class BetterCountMissing():
    def __init__(self):
        self.added = 0

    def __call__(self):
        self.added += 0
        return 0

counter = BetterCountMissing()
counter()

assert callable(counter)
