'''
1. map과 filter 보다는 리스트 comprehension을 사용하는게 명확함.
2. 딕셔너리도 가능함.
'''
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [x**2 for x in a]
squares

#람다와 리스트컴프리헨션을 이용해서
even_squares = [x**2 for x in a if x % 2 == 0]
alt = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, a)))
alt
assert even_squares == alt
alt
even_squares

#딕셔너리도 가능함.
chile_ranks = {'ghost': 1, 'habanero': 2, 'cayenne': 3}
rank_dict = {rank: name for name, rank in chile_ranks.items()}
rank_dict
#이름의 길이 구하기.
chile_len_st = {len(name) for name in rank_dict.values()}
chile_len_st


'''
1. 리스트 컴프리헨션은 다중 루프와 다중 조건을 지원함.
2. 표현식이 두개가 넘게 있으면 이해하기 어려우므로 피해야함.
'''

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#앞에 나온 for 문 부터 풀어 나간다.
#[1, 2, 3] 으로 먼저 한 행씩 가져오고, 1,2,3 으로 한 열씩 x로 가져온다.
flat = [x for row in matrix for x in row]
flat

#matrix 에 [1,2,3]을 먼저 꺼내어 row에 담는다. => row 값을 꺼낸뒤 제곱시킨후 리스트로 만든다.
squared = [[x**2 for x in row] for row in matrix]
squared

my_lists = [
    [[1, 2, 3], [4, 5, 6]]
]
flat = [x for sublist1 in my_lists
        for sublist2 in sublist1
        for x in sublist2]
flat

#물론 for 문 뿐만 아니라 if 문, and 문도 지원함
a = [x+1 for x in range(10)]
a
b = [x for x in a if x > 4 if x % 2 == 0]
b
c = [x for x in a if x > 4 and x % 2 == 0]
c

#합이 10 이상 3으로 나누어 떨어지는 셀 구하기
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#로우의 합이 10 이상인것 중에서, [3으로 나누어떨어지는 리스트를 x에 넣음]
filltered = [[x for x in row if x % 3 == 0]
             for row in matrix if sum(row) >= 10]
filltered
