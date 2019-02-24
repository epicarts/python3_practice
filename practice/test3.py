list1 = [5, 4, 1, 3, 2]
n = len(list1)
n
for i in range(1, n):
    mini=i
    for j in range(i-1, -1, -1):
        if list1[mini]<list1[j]:
            list1[j], list1[mini] = list1[mini], list1[j]
            mini=j

    print(list1)
list1#1
list1#-1

list = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
# 왼 => 오 , 현재 선택된 값 보다 큰 값을 선택.
# 오 <= 왼 ,
p = 0# 기준이 되는 피벗
low = p + 1# left ===> right
high = len(list)-1# left <=== rignt


#가장 작은 값과 가장 큰 값을 입력받아야함.
def quick_sort(list, left_index, right):

    #왼쪽부터 값이 피봇보다 작으면 계속 전진하다가
    if list[p] <= list[low]:
        low += 1
    #값이 큰게 나오면 high을 움직여야함.
    else:
        high -= 1
        #가다가 값이 피봇보다 작으면 교환.
    #교체 ?어떻게?



#전역 변수
list = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]

#함수 하나 들어갈 때, 바라는건 최종적인 pibot의 위치.
def quick_sort(list, left, right):
    p = left#처음 pivot 값은 가장 왼쪽에 있는 배열로 초기화
    left = p+1
