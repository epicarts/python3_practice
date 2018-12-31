a = ['a', 'b', 'c', 'd', 'e']
a[:4]
a[-4:]
a[2:-2]


#assert ?
#뒤의 조건이 참이면 오류를 내지 않음.
#만약 참이 아니면 오류가 나옴
#원하는 조건의 변수 값을 보증받을 때까지 assert로 테스트 할 수 있음.
#원하는 값인지 아닌지 테스트 할때 사용(굳이 if문 을 쓰지 않고 테스트 할수 있다고 생각함.)
assert a[:5] == a[0:5]

assert a[5:] == a[5:len(a)]

a[:]
a[:5]
a[:-1]
a[4:]
a[-3:-1]

#최대길이를 코드로 쉽게 설정할 수 있음.
#경계를 받어나도 적절하게 처리함
a[:20]

#슬라이싱의 결과는 완전히 새로운 리스트임
b = a[4:]
b
b[0] = 'z'
a
b

a[2:6] = [1,2]
a

a = b[:] #우너본 리스트의 복사
a

a = '2'
b
a

a = ['a', 'b', 'c', 'd', 'e']

odds = a[::2]#두칸씩 가져오기
odds
evens = a[1::2]#1 부터 두칸씩 가져오기
evens
x = 'mongose' #바이트로 저장
type(x)

x = b'mongose' #바이트로 저장
type(x)
y = x[::-1]
y

w ='뷝뷃'
x = w.encode('utf-8')
x
y = x[::-1]
y
z = y.decode('utf-8')#UTF-8 바이트 인코드된 유니코드 문자에서는 원하는 대로 동작하지 않음.

a
a[::-2]

somelist[start:end:stride간격]
b = a[::2]
c = b[1:-1]
c

#슬라이싱 => 스트라이딩 / 데이터의 앝은 복사본
