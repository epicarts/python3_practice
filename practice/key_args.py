'''
키워드 인수
1. 코드를 처음보는사람이 함수호출을 명확하게 이해 할 수 있다.
2. 함수를 정의 할때 기본값을 설정 할 수 있다는 점.

이런 선택적인 키워드 인수를 사용하면
*args를 인수로 받는 함수에서 하위 호환성을 지키기 어렵다.
키워드 전용 인수를 사용 하는 것.

'''

def remainder(number, divisor):
    return number % divisor

assert remainder(20, 7) == 6

remainder(20, 7)
remainder(20, divisor=7)
remainder(divisor=7, number=20)

remainder(number=20, 7)#위치 인수는 키워드 인수 앞에 지정해야함

remainder(7, number=20)#각 인수는 한번만 지정할수 있음

#인수에 기본값을 설정하였음
def flow_rate(weight_diff, time_diff, period=1):
    return (weight_diff / time_diff) * period

flow_per_second = flow_rate(weight_diff=0.5, time_diff=1)

flow_per_hour = flow_rate(weight_diff=0.5, time_diff=1, period=3600)

flow_per_hour
