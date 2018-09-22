'''
가운데 글자 가져오기
https://programmers.co.kr/learn/courses/30/lessons/12903
단어 s의 가운데 글자를 반환하는 함수
단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.
'''
s = "qwer"
len(s)
s[int(len(s)/2)] + s[int(len(s)/2)-1]


def solution(s):
    if len(s) % 2 == 0:
        return s[int(len(s)/2)-1] + s[int(len(s)/2)]
    else:
        return s[int(len(s)/2)]
