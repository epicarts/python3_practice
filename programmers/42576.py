'''
완주하지 못한 선수
https://programmers.co.kr/learn/courses/30/lessons/42576
'''
a = ["leo", "kiki", "eden","eden"]
b = ["eden", "kiki","leo"]
solution(a,b)

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]

    return participant[-1]

import collections
z = collections.Counter(a) - collections.Counter(b)
