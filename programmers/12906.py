'''
같은 숫자는 싫어
배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거

'''

a = [1,3,3,0,1,1]
[1,3,0,1]

def solution(arr):
    answer = []
    tmp = []
    for i in arr:
        if tmp is i:
            continue
        else:
            answer.append(i)
        tmp = i
    return answer
