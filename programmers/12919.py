'''
서울에서 김서방 찾기
seoul의 element중 Kim의 위치 x를 찾아,
김서방은 x에 있다는 String을 반환하는 함수
'''

seoul = ["Jane", "Kim"]
any(seoul)

seoul.index('Kim')
"김서방은 {}에 있다".format(next(i for i, s in enumerate(seoul) if s is 'Kim'))

def solution(seoul):
    return "김서방은 {}에 있다".format(next(i for i, s in enumerate(seoul) if s is 'Kim'))
