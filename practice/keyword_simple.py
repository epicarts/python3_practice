'''
키워드 인수는 함수 호출의 의도를 더 명확하게 해줌.
bool 플래그를 여러개 받는 함수처럼 헷갈릴때 사용하쟈!
파이썬 2는 **kwargs 를 사용한뒤 TypeError 예외를 일으키는 방법으로 흉내 내야함
'''

#나는 0으로 나눌때도 무시하고 싶고, 오버플로우도 무시하고 싶다.
def safe_division(number, divisor, ignore_overflow, ignore_zero_division):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise

#이렇게 보내는건 혼동하기 쉬움
result = safe_division(1, 10**500, True, False)


def safe_division2(number, divisor, ignore_overflow=False, ignore_zero_division=False):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise

#이런 키워드는 인수가 선택적인 동작이라서 함수를 호출하는 쪽에서 인수로 의도를 명확하게 강요할 수 없음.
safe_division2(1, 10**500, ignore_overflow=True)
safe_division2(1, 0, ignore_zero_division=True)
safe_division2(1, 0, True)# 이러면 머가 True 인지 모름



def safe_division3(number, divisor, *, ignore_overflow=False, ignore_zero_division=False):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise

safe_division3(1, 10*500, True, False)#위치 인수를 사용하는 함수 호출은 동작 x
safe_division3(1, 0, ignore_zero_division=True)

try:
    safe_division3(1,0)
except ZeroDivisionError:
    pass#정상 동작
