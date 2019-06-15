import time
import matplotlib.pyplot as plt
import numpy as np

def fun_a(n):
    i = 2
    start_time = time.time()
    while (i * i <=n):
        i += 1
    end_time = time.time()
    #print(float(end_time - start_time))
    return float(end_time - start_time)

time_list = []
a = np.arange(10,10000000000,500000000)
for n in a:
    time_list.append(fun_a(n))

len(a)
len(time_list)
D:\github\python3_practice\practice
plt.figure(figsize=(9,9))
plt.scatter(a, time_list)
plt.show()


for i in range(1, 7):
    print(" ".join([str(x) for x in list(range(1, i+1))]))


for i in range(1, 7):
    print("  " * (7-i) + " ".join([str(x) for x in list(range(i, 0, -1))]))
