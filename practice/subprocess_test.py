'''
병행성(concurrency): 컴퓨터가 여러 일을 마치 동시에 하듯이 수행하는 것.
CPU 1개 컴퓨터 => 빠르게 프로그램을 변경 => 동시에 실행하는 거처럼 보임

병렬성(parallelism): 실제로 여러 작업을 동시에 실행.


'''
import subprocess
import sys
from time import time

'''
proc = subprocess.Popen([sys.executable,'D:\\github\\python3_practice\\practice\\print_process.py'],
                        stdout=subprocess.PIPE)

#predict output is 'hello'
out, err = proc.communicate()
#from out string
print(out.decode('utf-8'))

#자식 프로세스는 부모 프로세스와 파이썬 인터프리터와는 독립적으로 실행됨.
#자식 프로세스는 다른 작업을 하는 동안 주기적으로 polling 됨
while proc.poll() is None:
    print('Working..')
    #시간이 걸리는 작업 을 수행.

print('Exit status', proc.poll)
'''



def run_sleep(period):
    #proc = subprocess.Popen(['sleep', str(period)])
    proc = subprocess.Popen([sys.executable,'D:\\github\\python3_practice\\practice\\print_process.py'],
                            stdout=subprocess.PIPE)
    return proc#프로세스

start = time()
procs =[]
for _ in range(10):
    proc = run_sleep(0.1)
    procs.append(proc)
proc = run_sleep(0.1)\

for proc in procs:
    proc.communicate()
    end = time()
print('finished in %.3f ' % (end- start))
