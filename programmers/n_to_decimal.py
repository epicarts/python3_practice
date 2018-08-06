
'''
n진법을 10 진법 숫자로 변환하기.
ing ( '문자열', 기존의 진법)=> 10진수로 변환됨.
'''


num, base = map(int, input().strip().split(' '))
print(int(str(num),base))


int('0b100',0) #이진수도 됨.
