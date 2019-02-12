# Axes3D 객체를 생성 후 3차원 그래프를 그리는 멤버함수 호출방식
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def show_perceptron(w1 = 0.5, w2 = 0.5, b = -0.7):
    fig = plt.figure()#그림 생성
    ax = fig.add_subplot(111, projection='3d')
    #fig.set_size_inches(6, 6, 6)# 크기 셋팅
    X1 = np.arange(0.0, 1.0, 0.01)
    X2 = np.arange(0.0, 1.0, 0.01)
    X1, X2 = np.meshgrid(X1, X2)
    Z = b + X1*w1 + X2*w2

    # Plot the surface.
    ax.plot_surface(X1, X2, Z, linewidth=0)

    # Y가 0일때. b + W1X1 + W2X2 = 0
    ax.plot_surface(X1, X2, np.zeros([1,1]), linewidth=1)

    ax.set_xlim([0, 1])
    ax.set_ylim([0, 1])
    ax.set_zlim([-1, 1])
    ax.set_xlabel('X1')
    ax.set_ylabel('X2')
    ax.set_zlabel('Y')

    ax.invert_xaxis()
    ax.scatter(0, 0, (w1*0) + (w2*0) + b, c='r', marker='x')#계단 함수 적용전
    ax.scatter(0, 1, (w1*0) + (w2*1) + b, c='r', marker='x')#계단 함수 적용전
    ax.scatter(1, 0, (w1*1) + (w2*0) + b, c='r', marker='x')#계단 함수 적용전
    ax.scatter(1, 1, (w1*1) + (w2*1) + b, c='r', marker='o')#계단 함수 적용전

    #ax.scatter(0, 0, and_gate_bais(0,0), c='b', marker='x')#계단 함수 적용
    #ax.scatter(0, 1, and_gate_bais(0,1), c='b', marker='x')#계단 함수 적용
    #ax.scatter(1, 0, and_gate_bais(1,0), c='b', marker='x')#계단 함수 적용
    #ax.scatter(1, 1, and_gate_bais(1,1), c='b', marker='o')#계단 함수 적용

    plt.show()

show_perceptron()
