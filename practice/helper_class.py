class SimpleGradebook(object):
    def __init__(self):
        self._grades = {}#_grades 라는 이름의 빈 딕셔너리 생성

    def add_student(self, name):
        # {'name' : []} 형태로 추가 시킴.
        self._grades[name] = []#이름이 들어올경우 딕셔너리에 이름 키

    def report_grade(self, name, score):
        self._grades[name].append(score)#키를 찾아서 90의 값을 넣음

    def average_grade(self, name):
        grades = self._grades[name]
        return sum(grades) / len(grades)

book = SimpleGradebook()
book.add_student('Issac Newton')
book.report_grade('Issac Newton', 90)
book.average_grade('Issac Newton')
book._grades

test = {}
test['d'] = []
test

class BySubjectGradebook():
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = {}

    def report_grade(self, name, subject, grade):#새로운 과목이 들어올떄마다 추가시킴
        by_subject = self._grades[name]
        grade_list = by_subject.setdefault(subject, [])
        grade_list.append(grade)

    def average_grade(self, name):
        by_subject = self._grades[name]
        total, count = 0, 0
        for grades in by_subject.values():#전체 subject 값에 있는 값을 전부 가져옴
            total += sum(grades)#전부 합침.
            count += len(grades)#전체의 개수를 구함
        return total / count

book = BySubjectGradebook()
book.add_student('Alice')
book.report_grade('Alice', 'Math', 75)
book.report_grade('Alice', 'Gym', 90)
book.average_grade('Alice')
book.report_grade('Alice', 'Gym', 10)
book.average_grade('Alice')
book._grades


#성적 비중을 추가해보쟈
class WeightedGradebook():
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = {}

    def report_grade(self, name, subject, score, weight):#가중치를 추가 시킴
        by_subject = self._grades[name]
        grade_list = by_subject.setdefault(subject, [])
        grade_list.append((score, weight))

    def average_grade(self, name):
        by_subject = self._grades[name]
        score_sum, score_count = 0, 0
        for subject, scores in by_subject.items():#과목안에 있는 전체 값을 가져옴
            subject_avg, total_weight = 0, 0
            for score, weight in scores:
                # ...
        return score_sum / score_count

#더 복잡해짐. 의미도 명확하지 않음.
book.report_grade('Alice', 'Math', 80, 0.10)
'''
계층이 한단계가 넘는 중첩은 피해야 한다(딕셔너리 안에 딕셔너리)
여러 계층으로 중첩하면 다른 프로그래머들이 코드를 이해하기 어려움.
유지보수 극켬
복잡하다고 느끼는 즉시 => 클래스로 옮겨가야함
'''

grades = []
grades.append((95, 0.45))
# ...
total = sum(score * weight for score, weight in grades)#모든 가중치를 계산 후 더함.
total
total_weight = sum(weight for _, weight in grades)#튜플은 위치에 의존함. _, 를 사용해서 나눳음.
total_weight
average_grade = total / total_weight

grades = []
grades.append((95, 0.45, 'Great job'))
total = sum(score * weight for score, weight, _ in grades) #3개의 값을 반환
total
#튜플을 길게 하는 방식 또한 딕셔너리 계층을 깊게 하는 방식과 비슷하다.
#튜플의 item 이 2개 이상 넘어가면 다른 방법도 고려해야함.

import collections


#namedtuple 을 사용하면 불변 데이터 클래스를 쉽게 정의 할 수 있다.
Grade = collections.namedtuple('Grade', ('score', 'weight'))


class Subject(object):#단일 과목 클래스
    def __init__(self):
        self._grades = []

    def report_grade(self, score, weight):
        self._grades.append(Grade(score, weight))

    def average_grade(self):
        total, total_weight = 0, 0
        for grade in self._grades:
            total += grade.score * grade.weight
            total_weight += grade.weight
        return total / total_weight

class Student():#학생 클래스
    def __init__(self):
        self._subject = {}

    def subject(self, name):
        if name not in self._subject:#과목안에 이름이 없다면,
            self._subject[name] = Subject() # Subject 클래스 생성
        return self._subject[name]

    def average_grade(self):
        total, count = 0, 0
        for subject in self._subject.values():
            total += subject.average_grade()
            count += 1
        return total / count

class Gradebook():
    def __init__(self):
        self._students = {}

    def student(self, name):
        if name not in self._students:
            self._students[name] = Student()
        return self._students[name]


book = Gradebook()
albert = book.student('Alice')
math = albert.subject('Math')
math.report_grade(80, 0.10)
