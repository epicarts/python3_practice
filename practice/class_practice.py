'''
self: 메도스가 해당클래스의 인스턴스 인지 확인해 주기위한 장치

'''

#자동차 클래스 생성
class Car:
    def __init__(self, brand, color, year):
        self.board = brand
        self.color = color
        self.year = year

    def get_info(self):
        print("나는 부모클래스 입니다.")
        print("%s %s %s" % (self.board, self.color, self.year))

class CarEmployee(Car):#Car 클래스를 상속(inheritance)받음
    def get_info(self):#메서드 오버라이딩(overriding)
        print("자식클래스입니당")
    pass

car1 = Car("test1", "Red", 1992)
car1.get_info()

car2 = CarEmployee("test1", "Red", 1992)
car2.get_info()



a = dir(car1)
a
pprint(a)
