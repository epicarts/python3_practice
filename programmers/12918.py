'''
문자열 다루기 기본
https://programmers.co.kr/learn/courses/30/lessons/12918

'''
s = '3224'
len(s)

if len(s) == 4 or len(s) == 6 and int(s):
    print("ok")
try:
    pass
except Exception as e:
    raise
len(s) in (4,6)
s.isdigit()

def solution(s):
    try:
        return int(s) and len(s) == 4 or len(s) == 6
    except:
        return False
solution('113a2')
