'''
https://programmers.co.kr/learn/courses/30/lessons/42585?language=python3
쇠막대기

1. 쇠막대기는 자신보다 긴 쇠막대기 위에만 놓일 수 있음.
2. 쇠막대기를 다른 쇠막대기 위에 놓는경우 완전히 포함되도록 놓되 겹치지 않도록
3. 각 쇠막대기를 자르는 레이저는 적어도 하나는 존재
4. 레이저는 어떤 쇠막대기의 양 끝점과도 겹치지 않음

시간 초과 뜸....
'''

str = "()(((()())(())()))(())"
str = "((((((()))))))"
stack = []
raser_stack = []
pieces_count = 0

for number,i in enumerate(str):
    #print(number, '번째 시작 스택:',stack,'/',raser_stack, tmp)
    if stack == []:# 스택에 아무것도 없다면 스택을 쌓아라
        stack.append(i)
        tmp = i
        continue
    if tmp == '(':
        if i == ')': # 레이져 가동
            stack.pop()# 스택의 가장 위 제거
            raser_stack = [i+1 for i in raser_stack] #모든 스택에 레이저 횟수 추가
            print('레이져 ')

        if i == '(':# 나무 판자 1스택 쌓기
            raser_stack.append(0)#기둥 하나 추가
            stack.append(i)#스택쌓기

    else:# 이전 값이 ) 이고
        if i == ')': #
            while stack[-1] != '(':
                stack.pop()# '(' 나올때 까지 제거
            stack.pop()
            pieces_count += raser_stack.pop()+1 #조각이기 떄문에
            print("최상위 스택 제거")
        if i == '(':
            stack.append(i)#스택에 추가
    tmp = i#이전에 나온 값 저장
    print('종료 스택:',stack,'/',raser_stack, tmp)
pieces_count

def solution(str):
    stack = []
    raser_stack = []
    pieces_count = 0
    for number,i in enumerate(str):
        #print(number, '번째 시작 스택:',stack,'/',raser_stack, tmp)
        if stack == []:# 스택에 아무것도 없다면 스택을 쌓아라
            stack.append(i)
            tmp = i
            continue
        if tmp == '(':
            if i == ')': # 레이져 가동
                stack.pop()# 스택의 가장 위 제거
                raser_stack = [i+1 for i in raser_stack] #모든 스택에 레이저 횟수 추가

            if i == '(':# 나무 판자 1스택 쌓기
                raser_stack.append(0)#기둥 하나 추가
                stack.append(i)#스택쌓기

        else:# 이전 값이 ) 이고
            if i == ')': #
                while stack[-1] != '(':
                    stack.pop()# '(' 나올때 까지 제거
                stack.pop()
                pieces_count += raser_stack.pop()+1 #조각이기 떄문에
            if i == '(':
                stack.append(i)#스택에 추가
        tmp = i#이전에 나온 값 저장
    return pieces_count

#정답
def solution(arrangement):
    answer = 0
    stack = 0
    laseron = False
    for p in arrangement:
        if p == '(':
            laseron = True
            stack += 1
        else:
            if laseron==True:
                answer += stack-1
                laseron=False
            else:
                answer += 1
            stack -= 1

    return answer
