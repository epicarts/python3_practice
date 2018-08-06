'''
zip 은 튜플을 반환

* Asterisk  을 사용할때 .
출처 : https://mingrammer.com/understanding-the-asterisk-of-python/
1. 곱셈 및 거듭제곱
2. 리스트 or 튜플을 확장 할 때
3. 가변인자를 사용 할 때
4. 컨테이너 타입의 데이터를 unpacking 할 때
함수에 값을 전달할 때 *primes와 같이 전달하면 primes 리스트의 모든 값들이
unpacking되어 numbers라는 리스트에 저장된다. 만약 이를 primes 그대로 전달한다면
이 자체가 하나의 값으로 쓰여 numbers에는 primes라는 원소가 하나 존재하게 된다.
'''
#3. 가변인자를 사용 할 때
def save_ranking(*args, **kwargs):
    print(args)
    print(kwargs)
save_ranking('ming', 'alice', 'tom', fourth='wilson', fifth='roy')
# ('ming', 'alice', 'tom')
# {'fourth': 'wilson', 'fifth': 'roy'}

primes = [2, 3, 5, 7, 11, 13]
def product(*numbers):
    print(numbers)
    return numbers
product(*primes)
product(primes)

mylist = [ [1,2,3], [4,5,6], [7,8,9] ]
new_list = list(map(list, zip(*mylist)))
new_list

new_list = [[],[],[]]

for i in range(3):
    for j in range(3):
        new_list[i].append( mylist[j][i] )

new_list

mylist = [ [1,2,3], [4,5,6], [7,8,9] ]
new_list = list(map(list, zip(*mylist)))
list(zip(*mylist))
list(zip(mylist))


new_list

[list(a) for a in zip(*mylist)]
