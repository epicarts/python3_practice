from urllib.parse import parse_qs

'''
1. 파이썬의 문법을 이용하면 한줄짜리 금방만듬. but 코드가 복잡해지고 난잡해짐
2. 복잡한 표현식은 헬퍼 함수로 옮기는게 좋음.
3. if else 를 이용하면 or and 보다 읽기 수월함.
'''
#keep_blank_values = True 면 값이 없어도 등록됨. False 면 등록 안됨(사라짐)
my_values = parse_qs('red=5&blue=0&green=',keep_blank_values=True)

my_values
my_values

repr(my_values)

my_values.get('red')
a = my_values.get('not',[''])[0] or 0
my_values.get('green')

red = my_values.get('red',[''])[0] or 0
red
green = my_values.get('green',[''])[0] or 0
green
a = my_values.get('not',[''])[0] or 0
a

# if else 로 바꾸면 이렇게도 쓸 수 있음
red = int(red[0]) if red[0] else 0
red

#if else 를 풀어쓰면,
green = my_values.get('green',[''])
if green[0]:
    green = int(green[0])
else:
    green = 0

#헬퍼 함수를 만들어보자
def get_first_int(values, key, default = 0):
    found = values.get(key, [''])
    if found[0]:
        found = int(found[0])
    else:
        found = default
    return found

#무조건 짧은 코드를 만들기보다는 가독성을 선택하는게 나음.

get_first_int(my_values,'green')
get_first_int(my_values,'red')
