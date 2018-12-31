'''
range는 정수집합을 순회(iterate) 하는 루프를 순회 할때 유용
'''

import random
random_bits = 0
for i in range(64):
    if random.randint(0, 1): # 0과 1이 난수로 나옴
        #random_bits = 1 << i | random_bits
        random_bits |= 1 << i # 왼쪽으로 i만큼 이동. random_bits와 or 연산을 함
        print(random_bits)
random_bits |= 1 << 2
random_bits

flavor_list = ['vanilla', 'chocolate', 'pecan', 'strawberry']
for flavor in flavor_list:
    print('%s is delicious' % flavor)
for i in range(len(flavor_list)):
    flavor = flavor_list[i]
    print('%d: %s' % (i + 1, flavor))

#이렇게 쉽게 바꿀수 있다.
for i, flavor in enumerate(flavor_list):
    print('%d: %s' % (i + 1, flavor))
#더짧게도 가능하다
for i, flavor in enumerate(flavor_list, 1):
    print('%d: %s' % (i, flavor))
