'''
내장함수 zip 을 사용해보자

1.zip은 지연 제너레이터이다.
2.zip은 이터레이터 두개 이상을 감싼다.
3.zip 제너레이터는 각 이터레이터로 부터 다음값을 담은 튜플을 얻어온다.
4.파이썬2에서는 zip이 제너레이터가 아니다.=> 즉, 메모리를 많이 사용한다.(itertools 에 있는 izip을 사용하면됨)

'''
names = ['apple', 'banana', 'mike']
letters = [len(name) for name in names]
letters

longest_name = None
max_letters = 0

#names 리스트의 길이만큼 반복 / 3회
for i in range(len(names)):
    count = letters[i]
    if count > max_letters:
        longest_name = names[i]
        max_letters = count
longest_name
max_letters
#가장 긴 이름은 banana 이며 길이는 6이다

#enumerate를 사용해보자
for i, name in enumerate(names):
    count = letters[i]
    if count > max_letters:
        longest_name = names[i]
        max_letters = count

#zip을 사용해보자
#입력 이터레이터들의 길이가 다르면 zip이 이상하게 동작함.
names
letters
for name, count in zip(names, letters):
    if count > max_letters:
        longest_name = names[i]
        max_letters = count

#이름을 append 하여 제너레이터 길이를 다르게 사용해보자
names.append('rosalind')
names
for name, count in zip(names, letters):
    print(name)
