class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        print("{0} 객체가 생성되었습니다.".format(self.__name))

    def __del__(self):
        print("{0} 객체가 제거되었습니다.".format(self.__name))

    def to_str(self):
        return "{0}\t{1}".format(self.__name, self.__age)

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age < 0:
            raise TypeError("나이는 0이상의 값만 허용합니다.")
        self.__age = age

    def create(self):
        return
#
# member = Person("홍길동", 20)
#
# if isinstance(member, Person):
#     print("member 는 Person 클래스의 인스턴스 입니다.")
#
# print(dir(member))

members = [
    Person("홍길동", 20),
    Person("이순신", 45),
    Person("강감찬", 35)
]
print(members)

members[0].set_age(-29)

for member in members:
    print(member.to_str())
