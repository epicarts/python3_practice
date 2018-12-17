'''
https://programmers.co.kr/learn/courses/30/lessons/12917
문자열 내림차순으로 배치하기
문자를 큰것부터 작은 순으로 정렬해 새로운 문자열을 리턴하는 함수
대문자는 소문자보다 작은 것으로 간주합니다.
'''
s1 = "Zbcdefg"
''.join(sorted(s1,reverse = True))

def solution(s):
    return ''.join(sorted(s,reverse = True))
