


class MyBaseClass():
    def __init__(self, value):
        self.value = value

class MyChildClass():
    def __init__(self):
        MyBaseClass.__init__(self, 5)#직접 호출하는 행위는 삼가..

class TimesTwo():
    def __init__(self):
        self.value *= 2

class PlusFive():
    def __init(self):
        self.value += 5

class OneWay(MyBaseClass, TimesTwo, PlusFive):#기본 => 곱셈 => 더하기
    def __init__(self, value):
        MyBaseClass.__init__(self, value)#5를 부르고
        TimesTwo.__init__(self)#2를 곱하고
        PlusFive.__init__(self)# 5를 더하는 값 예상

foo = OneWay(5)
#(5 * 2) + 5 = 10?? 15가 안나옴 어째서???? 객체를 따로 참조하나 ..
foo.value

class AnotherWay(MyBaseClass, PlusFive, TimesTwo):#부모 클래스를 다른 순서로 정의함
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        TimesTwo.__init__(self)
        PlusFive.__init__(self)

#다이아몬드 상속
bar = AnotherWay(5)
bar.value


class TimesFive(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        self.value *= 5

class PlusTwo(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        self.value += 2

class ThisWay(TimesFive, PlusTwo):
    def __init__(self, value):
        TimesFive.__init__(self, value)
        PlusTwo.__init__(self, value)#호출 두번째 호출될떄 자동으로 self.value를 리셋함

foo = ThisWay(5)
#self.value를 다시 5로 리셋함
foo.value

#파이썬 3 에서는 super를 인수 없이 호출하면 __class__와 self를 인수로 넘겨서 호출.
#파이썬 3에서는 항상 super을 사용해야함.
class Explicit(MyBaseClass):
    def __init__(self, value):
        super(__class__, self).__init__(value * 2)

class Implicit(MyBaseClass):
    def __init__(self, value):
        super().__init__(value * 2)

Explicit(10).value
Implicit(10).value
