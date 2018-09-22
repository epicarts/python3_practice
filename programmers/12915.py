'''
https://programmers.co.kr/learn/courses/30/lessons/12915?language=python3
문자열 내 마음대로 정렬하기

각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬하려 합니다.
strings가 [sun, bed, car]이고 n이 1이면
각 단어의 인덱스 1의 문자 u, e, a로 strings를 정렬
'''
strings =["abzcd","cdzab","abzfg","abzaa","abzbb","bbzaa",'sun', 'bed', 'car']
solution(["abzcd","cdzab","abzfg","abzaa","abzbb","bbzaa"],2)

sorted(strings)
#abzaa abzbb 가 나와야함.
#n번째 있는 걸로 비교 후. 같은게 있을 경우 그것을 사전순으로 정렬.

answer = [strings[char_list[1]] for char_list in char_list]
#알파벳 a-z 까지
#3번째 알파벳이 같은것 끼리 비교 후 sorted

#사기...;;
sorted(strings, key=lambda x: x[2])

import string

def solution(strings, n):
    sorted(strings)
    char_list = sorted([(string[n],i) for i,string in enumerate(strings)])
    answer = [strings[char_list[1]] for char_list in char_list]
    return answer
