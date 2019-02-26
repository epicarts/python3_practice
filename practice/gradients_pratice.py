def getF(x):
    a = 0.5
    b = 0.1
    return a*x + b

getF(1)#직선을 그림.
getF(1.1)#0.1만큼 이동

x = 1.0
dx = 0.1
df = getF(x + dx) - getF(x)
df_over_df = df / dx
df_over_df



x = 1.0
dx = 0.1
dx_target = 0.2
df = getF(x + dx) - getF(x)

df = getF(x + dx) - getF(x)
dfdx = df / dx
f_new = getF(1.0) + dfdx * dx_target

#비교해보쟈
getF(x + dx_target)
f_new


#델타 X 값을 얼마나 움직여야 원하는 f_target 이 나올 것인가
x = 1.0
dx = 0.1
df = getF(x + dx) - getF(x)
dfdx = df / dx

f_target = 0.7
dx_traget = (f_target - getF(x)) / dfdx

#비교해보쟈
f_target
getF(x + dx_target)
dx_target



##미분 방식 두개를 섞어보쟈 미분이 가능하면 직접 넣는게 연산이 빠름
def getFx(x):
    a = 0.5
    b = 0.1

    return a # 미분값은 기울기 이므로 기울기 반환

x = 1.0
fx = getFx(x)

f_target = 0.7
dx_target = (0.7 - getF(x)) / fx

f_target
getF(x+ dx_target)

class MyFunction():
    def __init__(self, x):
        self.a = 0.0
        self.b = 0.0
    def getvalue(self, x):
        return self.a*x + self.b
