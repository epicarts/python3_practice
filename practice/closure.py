'''
클로저란?
자신이 정의된 스코프에 잇는 변수를 참조하는 함수

숫자 리스트를 정렬 => 특정 그룹 숫자들이 먼저오도록 우선순위
사용자 인터페이스를 표현 or 중요한 메시지나 예외 이벤트를 먼저 보여줘야 할때

일반적인 방법
sort메서드의 헬퍼함수를 key 인수로 넘김.
헬퍼 반환 값 => 리스트에있는 각 아이템을 정렬

변수를 참조할때 스코프(scope) 를 탐색<우선순위>
1. 현재 함수의 스코프
2. (현재 스코프를 담고 있는 다른 함수)감싸고 있는 스코프
3. 코드를 포함하고 있는 모듈의 스코프(전역)
4. (len or str 같은 함수)내장 스코프
'''
def sort_priority(values, group):
    #파이썬에서 함수는 일급 객체이다.
    def helper(x):#클로저가 적용됨(group인수에 접근 가능)
        if x in group:
            return (0, x)#만약 group안에 값이 있으면 0을 리턴
        return (1, x)#1을 리턴
    values.sort(key=helper)

numbers = [9, 2, 5, 6, 2, 7, 1]
group = {2, 3, 5, 7}
sort_priority(numbers, group)
print(numbers)


#우선순위가 높은 아이템을 발견했을 때 플래그를 뒤집어보자 (실패)
def sort_priority2(values, group):
    found = False#sort_priority2에 found 변수 생성
    def helper(x):#클로저가 적용됨(group인수에 접근 가능)
        if x in group:
            found = True# helper 클로저에서 True로 할당 된다. 즉, 새로운 변수임
            return (0, x)#만약 group안에 값이 있으면 0을 리턴
        return (1, x)#1을 리턴
    values.sort(key=helper)
    return found

found = sort_priority2(numbers, group)
found#정렬된 결과를 올바르지만 false가 뜸


#파이썬 3에서 클로저에서 데이터를 얻어오는 문법(nonlocal)
def sort_priority3(numbers, group):
    found = False
    def helper(x):
        nonlocal found#클로저에서 데이터를 다른 스코프에 할당
        if x in group:
            found = True
            return (0, x)
        return (1, x)
    numbers.sort(key=helper)
    return found

#클래스를 활용한 방법
class Sorter(object):
    def __init__(self, group):#전체를 초기화
        self.group = group
        self.found = False

    def __call__(self, x):
        if x in self.group:
            self.found = True
            return (0, x)
        return (1, x)

sorter = Sorter(group)#Sorter 클래스의 객체 생성
numbers.sort(key = sorter)
assert sorter.found is True
