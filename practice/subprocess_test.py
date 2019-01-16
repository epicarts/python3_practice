'''
병행성(concurrency): 컴퓨터가 여러 일을 마치 동시에 하듯이 수행하는 것.
CPU 1개 컴퓨터 => 빠르게 프로그램을 변경 => 동시에 실행하는 거처럼 보임

병렬성:
'''
import subprocess
import sys

proc = subprocess.Popen([sys.executable,'D:\\github\\python3_practice\\practice\\print_process.py'],
                        stdout=subprocess.PIPE)
'''
#predict output is 'hello'
out, err = proc.communicate()
#from out string
print(out.decode('utf-8'))
'''

while proc.poll() is None:
    print('Working..')
    #시간이 걸리는 작업 을 수행.

print('Exit status', proc.poll)
