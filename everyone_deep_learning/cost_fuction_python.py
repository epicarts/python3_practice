import numpy as np

X = np.array([1, 2, 3])
Y = np.array([1, 2, 3])

def cost_func(W, X, Y):
    c = 0
    for i in range(len(X)):
        # 기울기 * x값
        h = W * X[i]
        c += (h - Y[i]) ** 2 #(예측값 - 실제값)^2
    return c/len(X) # 평균 구하기

#W 값을 -3 ~ 5 개 15구 소수 셋쨰자리까지
for feed_W in np.linspace(-3, 5, num=15):
    curr_cost = cost_func(feed_W, X, Y)
    #10칸띄고
    print("{:10.3f}|{:10.5f}".format(feed_W, curr_cost) )
