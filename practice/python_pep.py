'''
파이썬 코딩의 기술 책을 이용해서 파이썬 사용해보기
https://www.python.org/dev/peps/pep-0008/
# 한줄의 문자길이가 79자 이하
12345678901234567890123456789012345678901234567890123456789012345678901234567890
#스페이스바 4개 이용하여 들여쓰기

'''

#변수, 함수, 속성
lowercase_underscore

#보호(protected)
_leading_underscore

#비공개(private)
__double_leading_underscore

#클래스
CapitalizedWord

#모듈 수준 상수
ALL_CAPS

#길이를 확인 하여 빈값을 확인하지 않음.
#no if len(somelist) == 0
#yes if somelist

#항상 맨위에 import 를 넣는다
import mypkg.sibling
from mypkg import sibling
from mypkg.sibling import example

#모듈을 호출할때 정활히
import foo #no
from boo import foo #yes

#상대적인 임포트를 해야한다면
from . import foo



foo = long_function_name(var_one, var_two,
                         var_three, var_four)

#스페이스8개
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

#NO
import os, sys

#yes
import os
import sys


#YES
span(ham[1], {eggs: 2})
foo = (0,)
if x == 4: print(x, y; )
#NO
span( ham[ 1 ], { eggs: 2 } )
bar = (0, )
