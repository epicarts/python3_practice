class Person:
    count = 0

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        print("{0} 객체가 생성되었습니다.".format(self.__name))
        Person.count = Person.count + 1

    def __del__(self):
        print("{0} 객체가 제거되었습니다.".format(self.__name))

    def to_str(self):
        return "{0}\t{1}".format(self.__name, self.__age)

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 0:
            raise TypeError("나이는 0이상의 값만 허용합니다.")
        self.__age = age

    @classmethod
    def get_info(cls):
         # 클래스 참조정보가 인자로 넘어오는 매개변수
        return "현재 Persion 클래스의 인스턴스는 총 {0}개 입니다.".format(cls.count)

    #비교 연산자 오버로딩
    def __gt__(self, other):
        return self.__age > other.__age

    def __ge__(self, other):
        return self.__age >= other.__age

    def __lt__(self, other):
        # self의 age 가 other의 age보다 작으면 true 반환
        return self.__age < other.__age

    def __le__(self, other):
        # self의 age 가 other의 age보다 작거나 같으면 true 반환
        return self.__age <= other.__age

    def __eq__(self, other):
        return self.__age == other.__age

    def __ne__(self, other):
        return self.__age != other.__age

    def __str__(self):
        #문자열 반환
        return "{0}\t{1}".format(self.__name, self.__age)


members = [
    Person("홍길동", 20),
    Person("이순신", 45),
    Person("강감찬", 35)
]

cnt = len(members)
i = 0
while True:
    print("members[{0}] > members[{1}] => {2}".format(i, i + 1, members[i] > members[i + 1]))
    i += 1
    if i == cnt -1:
        print("members[{0}] > members[{1}] => {2}".format(i, 0, members[i] > members[0]))
        break

print(members)

members[0].age = 555

print(Person.get_info())

for member in members:
    print(member.to_str())
    print(str(member))


print("현재 Persion 클래스의 인스턴스는 총 {0}개 입니다.".format(Person.count))
