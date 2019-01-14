


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

class OneWay(MyBaseClass, TimesTwo, PlusFive):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)#5를 부르고
        #TimesTwo.__init__(self)#2를 곱하고
        PlusFive.__init__(self)# 5를 더하는 값 예상

foo = OneWay(1)
#(5 * 2) + 5 = 10?? 15가 안나옴
foo.value
foo = PlusFive()
