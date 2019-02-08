'''
앞에서부터 읽을 때나 뒤에서부터 읽을 때나 모양이 같은 수를 대칭수(palindrome)
두 자리 수를 곱해 만들 수 있는 대칭수 중 가장 큰 수는 9009 (= 91 × 99) 입니다.
세 자리 수를 곱해 만들 수 있는 가장 큰 대칭수는 얼마입니까?
'''

right_max = 999
left_max = 999

switch =1
for i in range(999,0,-1):
    for j in range(999,0,-1):
        result = i * j
        result_len = int(len(str(result))/2)
        if str(result)[0:result_len] == str(result)[:result_len-1:-1]:
            switch = 0
            break
    if switch is 0:
        break
print("정답: ",j ,i)
