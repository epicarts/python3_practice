import time
import matplotlib.pyplot as plt
import numpy as np

def fun_a(n):
    i = 2
    start_time = time.time()
    while (i <=n):
        i += 1
    end_time = time.time()
    #print(float(end_time - start_time))
    return float(end_time - start_time)

time_list = []
a = np.arange(1,1000000,1000)
for n in a:
    time_list.append(fun_a(n))

len(a)
len(time_list)
plt.figure(figsize=(9,9))
plt.scatter(a, time_list)
plt.show()
