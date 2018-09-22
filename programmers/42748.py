'''
https://programmers.co.kr/learn/courses/30/lessons/42748
K번째수
배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때,
 k번째에 있는 수를 구하려 합니다.
'''
array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
for command in commands:
    sorted(array[command[0] - 1:command[1]])[command[2]-1]

def solution(array, commands):
    answer = []
    for command in commands:
        answer.append(sorted(array[command[0] - 1:command[1]])[command[2]-1])
    return answer
