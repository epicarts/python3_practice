'''
텍사스 주의 여행자 수를 분석
1. 데이터 집합은 각 도시의 방문자수(백만명 단위)=> 각 도시에 여행자가 몇퍼센트?
2. 정규화 함수 => 연도별 총 여행자 수를 구함.
3. 각 도시의 방문자 수/전체 방문자 수

'''

def normalize(numbers):
    total = sum(numbers)#모든 숫자의 합을 구함
    result = []
    for value in numbers:# 도시 개별의 값으로 for문
        percent = 100 * value / total
        result.append(percent)#각 계산한 식을 append를 이용하여 리스트에 추가
    return result

visits = [15, 35, 80]
percentages = normalize(visits)
percentages

#제너레이터로 변경
def read_visits(data_path):
    with open(data_path) as f:#데이터 경로를 열고.
        for line in f:
            yield int(line)
it = read_visits('text.txt')
#될거라고 생각했지만 안됨. => 이터레이터가 결과를 한번만 생성하기 때문
percentages = normalize(it)
percentages

list(it)
list(it)#두번 사용하면 이미 사라져 있음.

#StopIteration 예외가 일어나지 않았다. => 입력 이터레이터를 명시적으로 소진해야함
#전체 콘텐츠의 복사본을 리스트에 저장해야함.

def normalize_copy(numbers):
    numbers = list(numbers) # 이터레이터를 복사함 => 복사본이 클 수도 있음.
    total = sum(numbers)#모든 숫자의 합을 구함
    result = []
    for value in numbers:# 도시 개별의 값으로 for문
        percent = 100 * value / total
        result.append(percent)#각 계산한 식을 append를 이용하여 리스트에 추가
    return result

it = read_visits('text.txt')
percentages = normalize_copy(it)
percentages


#이터레이터 복사로 인한 메모리 고갈을 피하는 방법
#호출될때마다 새 이터레이터를 반환하는 함수를 만든다
def nomalize_func(get_iter):
    #하나의 이터레이터를 이용하지 않고 새롭게 이터레이터를 각각 불러옴
    #다 합칠 이터레이터 즉 여기서는 전부 꺼낸뒤 합침
    total = sum(get_iter())#이터레이터를 하나씩 불러옴.새 이터레이터
    result = []
    for value in get_iter():#새 이터레이터 여기서는 for문 한번씩 돌릴때마다 이터레이터 호출
        percent = 100 * value /total
        result.append(percent)
    return result

#잘 동작하나 람다 함수를 넘겨주는 방법은 별로임.
percentages = nomalize_func(lambda: read_visits('text.txt'))
percentages

'''
더 좋은 방법은 이터레이터 프로토콜(iterator protocol)을 구현한 새 컨테이너 클래스를 제공

'''
# iter(foo)를 호출 => iter은 foo.__iter__를 호출 => __iter__ 메서드는 이터레이터 객체를 반환
#for 루프는 StopIteration예외가 발생할 때까지 이터레이터 객체에 내장함수 next를 계속 호출
for x in foo:
    print(x)


#구현해보쟈
class ReadVisits(object):
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:#입력데이터를 여러번 불러오는게 단점.
            for line in f:
                yield int(line)

def normalize(numbers):
    #sum 메서드가 새 이터레이터 객체를 할당하려고 ReadVisits.__iter__를 호출함
    total = sum(numbers)
    result = []
    for value in numbers:# 도시 개별의 값으로 for문
        percent = 100 * value / total
        result.append(percent)#각 계산한 식을 append를 이용하여 리스트에 추가
    return result

visits = ReadVisits('text.txt')#class 객체 생성
percentages = normalize(visits)
percentages
