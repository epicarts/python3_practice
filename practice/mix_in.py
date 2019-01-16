'''
다중 상속으로 얻는 편리함과 캡슐화가 필요 하다 => mix_in 을 작성

mix_in?
클래스의 추가적인 메서드만 정의하는 작은 클래스
자체 인스턴스속성(atrribute)를 정의 X
__init__ 생성자를 호출하도록 요구하지 않음

현재 상태를 간단하게 조사할 수 있음 => 믹스인을 쉽게 작성가능
dynamic inspection(동적 조사)
'''

#
class ToDictMixin():
    def to_dict(self):
        return self._traverse_dict(self.__dict__)

    def _traverse_dict(self, instance_dict):#dict 형식의 객체가 들어온다면
        output = {}
        for key, value in instance_dict.items():#dict 안에 있는 key와 value 를꺼내서
            output[key] = self._traverse(key, value)#_travers 함수에 전달
        return output

    #난이도... 너무 높아 ....ㅠㅠ
    def _traverse(self, key, value):#key와 value 를 받음
        #isinstance => 동적 타입 검사
        if isinstance(value, ToDictMixin): #value 가 ToDictMixin타입의 객체라면.
            return value.to_dict()#ToDictMixin 안에 있는 메소드 to_dict함수를 반환함.
        elif isinstance(value, dict):#만약 dic 타입이라면
            return self._traverse_dict(value)
        elif isinstance(value, list):#list instance 라면,
            return [self._traverse(key, i) for i in value]#값을 분해해서 자기자신에게 넣음.
        elif hasattr(value, '__dict__'):#hasattr를 사용한 동적접근 ?
            return self._traverse_dict(value.__dict__)
        else:
            return value



class BinaryTree(ToDictMixin):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

tree = BinaryTree(10,
                  left=BinaryTree(7, right=BinaryTree(9)),
                  right=BinaryTree(13, left=BinaryTree(11)))
tree.to_dict()
# 순환 참조는 ToDictMixin.to_dict 의 기본 구현이 무한 루프에 빠짐게 만듬

class BinaryTreeWithParent(BinaryTree):#BinaryTree 클래스의 자식노드
    def __init__(self, value, left=None,
                 right=None, parent=None):
        #super(): 슈퍼클래스의 method를 호출,
        #다수의 슈퍼 클래스가 존재: 호출 순서는 __mro__ 를 통해 결정
        #전체 클래스의 상속구조를 이해하지 못하였어도 ㄱㅊ
        super().__init__(value, left=left, right=right)
        self.parent = parent

    #_traverse 메서드를 오버라이드 해서 부모를 탐색하지 않고, 부모의 숫자 값만 꺼내옴
    def _traverse(self, key, value):
        #같은 타입의 속성이 들어온다면 if문
        if (isinstance(value, BinaryTreeWithParent) and key == 'parent'):
            return value.value
        else:#아니면 새로 root를 만들어야함.
            return super()._traverse(key, value)

root = BinaryTreeWithParent(10)
root.left = BinaryTreeWithParent(7, parent=root)
root.left.right = BinaryTreeWithParent(9, parent=root.left)
root.to_dict()
#BinaryTreeWithParent._traverse 덕분에 BinaryTreeWithParent 클래스면 자동으로
#ToDictMixin으로 동작함.

class NamedSubTree(ToDictMixin):#부모개 ToDictMixin
    def __init__(self, name, tree_with_parent):
        self.name = name
        self.tree_with_parent = tree_with_parent

my_tree = NamedSubTree('Foobar', root.left.right)
my_tree.to_dict() #무한루프를 돌지 않음.


class JsonMixin():
    '''
    classmethod 와 instancemethod 둘다 정의 하였다.
    믹스인을 이용하면 두 종류의 동작을 추가 할 수 있다.
    요구사항 : 클래스에 to_dict 메서드가 있고, 해당 클래스의 __init__ 메서드에서 키워드 인수를 받음.
    '''
    @classmethod
    def from_json(cls, data):
        kwargs = json.loads(data)
        return cls(**kwargs)

    def to_json(self):
        return json.dumps(self.to_dict())#to_dict호출

import json
import switch_case
from switch import Switch

class DatacenterRack(ToDictMixin, JsonMixin):
    def __init__(self, switch=None, machines=None):
        self.switch = Switch(**switch)
        self.machines = [machine(**kwargs) for kwargs in machines]
class Switch(ToDictMixin, JsonMixin):
    #...
    :

class Machine(ToDictMixin, JsonMixin):
    # ...
serialized = """{"switch": {"ports": 5, "speed": 1e9}, "machines": [{"cores": 8, "ram": 32e9, "disk": 5e12}]}"""

deserialzed = DatacenterRack.from_json(serialized)
roundtrip = deserialzed.to_json()
