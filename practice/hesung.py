import numpy as np
import matplotlib.pyplot as plt


def trans_fun(theta, F1):
    radian_theta = theta * np.pi / 180
    trans = np.array([[np.cos(radian_theta), -np.sin(radian_theta)],
                      [np.sin(radian_theta), np.cos(radian_theta)]])
    return np.dot(trans, F1.reshape(2,1)).reshape(2)

a = 9.81 # 중력임
m1 = 0.04# 추1 무게.
m2 = 0.04# 추2 무게.
m3 = 0.02# 추3 무게.
degree = [265.5, 14.5, 121]

bais = np.array([1.0,0.0]) # 기저 벡터 (1,0)

#F의 좌표값과 theta 를 넣으면 회전벡터가 나옴.
F1 = trans_fun(degree[0], bais)
F2 = trans_fun(degree[1], bais)
F3 = trans_fun(degree[2], bais)

#중력값과 추의 무게 고려하기
F1 = m1 * a * F1
F2 = m2 * a * F2
F3 = m3 * a * F3

#합벡터 좌표 구하기
R1 =  np.array([F1[0] + F2[0], F1[1] + F2[1]])# F1 + F2 = R1 합벡터
R2 =  np.array([R1[0] + F3[0], R1[1] + F3[1]])# R1 + F3 = R2 합벡터

#그래프 그리기

soa = np.array([F1, F2, F3])
U, V = zip(*soa)
plt.figure(figsize=(9,9))
ax = plt.gca()
#quiver (start x , start y, end x, end y)
ax.quiver([0, 0, 0],[0, 0, 0], U, V, angles='xy', scale_units='xy', scale=1)# F1, F2, F3
ax.quiver([F1[0], F2[0]], [F1[1], F2[1]], [F2[0], F1[0]], [F2[1], F1[1]],
          LineStyle='--',color ='gray', angles='xy', scale_units='xy', width = 0.005, scale=1)# F1, F2 관계표현

ax.quiver([0],[0], R1[0],R1[1], color ='red', angles='xy', scale_units='xy', scale=1)# F1 + F2 = R1 합벡터 표현

ax.quiver([0],[0], R2[0],R2[1], color ='blue', angles='xy', scale_units='xy', scale=1)# R1 + F3 관계 표현
ax.quiver([F3[0], R1[0]], [F3[1],R1[1]], [R1[0], F3[0]], [R1[1],F3[1]], width = 0.005, color ='gray', angles='xy', scale_units='xy', scale=1)# R1 + F3 관계 표현

ax.quiver([0],[0], R2[0],R2[1], color ='blue', angles='xy', scale_units='xy', scale=1)# R1 + F3 = R2 합벡터 표현


print("R1 vecotr: ", R1)
print("R2 vecotr: ", R2)

ax.set_xlim([-max(U) - 0.01, max(U) + 0.01])
ax.set_ylim([-max(R1) - 0.1, max(R1) + 0.01])
plt.draw()
plt.show()
