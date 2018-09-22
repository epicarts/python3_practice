'''
https://programmers.co.kr/learn/courses/30/lessons/12901
2016년
2016년 a월 b일은 실제로 있는 날입니다.
(13월 26일이나 2월 45일같은 날짜는 주어지지 않습니다)

'''
def solution(a, b):
    mon_2016 =[31,29,31,30,31,30,31,31,30,31,30,31]
    day = ["THU","FRI","SAT","SUN","MON","TUE","WED"]
    days = sum(mon_2016[:a - 1]) + b
    return day[days % 7]
