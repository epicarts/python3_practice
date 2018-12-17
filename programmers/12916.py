'''
https://programmers.co.kr/learn/courses/30/lessons/12916?language=python3
문자열 내 p와 y의 개수
s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True
다르면 False를 return
하나도 없는 경우는 항상 True
'''
s1 = "pPoooyY"
s2 = "Pyy"

low_s1 = s1.lower()
low_s1.count('p')
low_s1.count('y')

def solution(s):
    low_s = s.lower()
    return True if low_s.count('p') is low_s.count('y') else False
