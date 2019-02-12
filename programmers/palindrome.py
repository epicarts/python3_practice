'''
앞에서부터 읽을 때나 뒤에서부터 읽을 때나 모양이 같은 수를 대칭수(palindrome)
두 자리 수를 곱해 만들 수 있는 대칭수 중 가장 큰 수는 9009 (= 91 × 99) 입니다.
세 자리 수를 곱해 만들 수 있는 가장 큰 대칭수는 얼마입니까?
'''

right_max = 999#세자리 수 중 가장 큰 숫자인 999부터 시작
left_max = 999#세자리 수 중 가장 큰 숫자인 999부터 시작

switch = 1#두번째 for문을 탈출하기 위한 키워드
for i in range(999, 0, -1):#999, 998, 997, 996 ....1
    for j in range(999, 0, -1):#999, 998, 997, 996 ....1
        result = i * j#숫자를 곱한다.

        #곱한 결과가 1234 즉, 4자리면 2반환
        #곱한 결과가 12345 즉, 5자리면 2반환
        #곱한 결과가 123456 즉, 6자리면 3반환
        result_len = int(len(str(result))/2)

        #str(result)[0:result_len] 0번째 배열 ~ result_len 길이까지 반환
        #12345면, 12 를 반환
        #str(result)[:result_len-1:-1] 마지막 배열 ~ result_len-1 길이까지 반환
        #12345면, 54 를 반환
        if str(result)[0:result_len] == str(result)[:result_len-1:-1]:
            switch = 0#두번째 for문을 빠져나가기 위해 값을 변경함
            break

    #정답이 나왓으면 switch 값이 0으로 바꼇으므로 더이상 for문을 돌지 않고 탈출
    if switch is 0:
        break
print("정답: ",j ,i)
