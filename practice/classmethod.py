'''
파이썬에서는
객체: 다형성
클래스: 다형성

계층 구조에 속한 여러 클래스를 => 자체 메서드(독립적 버젼) 구현

여러 클래스가 같은 인터페이스나 추상기반 클래스를 충족하면서도 다른 기능을 제공함.
'''


#ex) 맵리듀스를 구현. => 입력데이터를 표현할 공통 클래스가 필요함.

#서브클래스에서 정의해야하는 read 메서드가 있는 입력 클래스
class InputData():
    def read(self):
        raise NotImplementedError

#파일에서 데이터를 읽어오도록 구현한 InputData()의 서브 클래스
class PathInputData(InputData):#부모클래스 InputData 객체를 가져옴
    def __init__(self, path):
        super().__init__() # 부모클래스의 __init__ 메소드 호출
        self.path = path

    def read(self):
        return open(self.path).read()

#InputData 가 메인 그 아래 서브 클래스로 PathInputData()
ㅁ 
