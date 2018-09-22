'''
모의고사
https://programmers.co.kr/learn/courses/30/lessons/42840
1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때,
 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return
'''

solution([1,2,3,4,5])
solution([1,3,2,4,2])

def solution(answers):
    result_list =[]
    math_1 = [1, 2, 3, 4, 5]
    math_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    math_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    math_1 = math_1 * round(len(answers)/len(math_1) + 0.5) #메모리 절약
    math_2 = math_2 * round(len(answers)/len(math_2) + 0.5)
    math_3 = math_3 * round(len(answers)/len(math_3) + 0.5)
    result_list.append(len([answer for i,answer in enumerate(answers)
                            if math_1[i] == answer]))#정답 개수 추출.
    result_list.append(len([answer for i,answer in enumerate(answers)
                            if math_2[i] == answer]))
    result_list.append(len([answer for i,answer in enumerate(answers)
                            if math_3[i] == answer]))
    return [i + 1 for i,result in enumerate(result_list)#추출된 결과중 가장 큰 index 만 추출
            if max(result_list) == result]
