'''
https://programmers.co.kr/learn/courses/30/lessons/42583
다리를 지나는 트럭
모든 트럭이 다리를 건너려면 최소 몇초가 걸리는지

길이가 2대까지 무게가 10kg까지 견디는 다리
7,4,5,6


견딜 수 있는 무게 - 현재 다리 위 무게
10 - 0  = 10 이하의 값을 올릴 수 있음
10 - 7  = 3 이하의 값을 올릴 수 있음
'''
from collections import deque
bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
truck_queue = deque(truck_weights)
bridge_queue = deque([])
count = 0
bridge_queue
while bridge_queue != truck_queue:#다리를 건너고 있는 트럭 = 대기트럭 둘다 비었으면
    print(count, bridge_queue,truck_queue)
    bridge_queue = deque([(i,j+1) for i,j in bridge_queue if j+1 is not bridge_length])

    #if bridge_queue:#만약 다리에 무언가 있다면,
        #1씩 건너는데, 현재 다리를 다 건너면 bridge_queue에서 제거
    #    bridge_queue = [(i,j+1) for i,j in bridge_queue if j+1 is not bridge_length]

    #다리 위로 올리는 if 문
    if truck_queue:#만약 출발 할 곳에 스택이 쌓여 있다면,
        #견딜 수 있는 무게 - 현재 다리무게 >= 지금 나올 차의 무게
        if (weight - sum(int(i) for i,j in bridge_queue)) >= truck_queue[0]:
            bridge_queue.append((truck_queue.popleft(),0))#트럭 큐 제거 => 다리큐 추가
        else:#다리에 아무것도 못 올라갈 경우
            print("wait")
    if 'a' == input():
        break
    #한턴 지날때 마다 truck_count 1씩 증가 시키기
    count += 1 #경과 시간 1초가 지나감


from collections import deque
def solution(bridge_length, weight, truck_weights):
    truck_queue = deque(truck_weights)
    bridge_queue = deque([])
    count = 0
    while bridge_queue != truck_queue:
        bridge_queue = deque([(i,j+1) for i,j in bridge_queue if j+1 is not bridge_length])
        if truck_queue and (weight - sum(int(i) for i,j in bridge_queue)) >= truck_queue[0]:
            bridge_queue.append((truck_queue.popleft(),0))
        count += 1
    return count
solution(2,10,[7,4,5,6])
