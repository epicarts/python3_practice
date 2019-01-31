import numpy as np


def f(x, y, z):
    return (x + y) / z

result = f(5, 6, 7.5)

a = np.random.randn(10, 10)
%timeit np.dot(a, a)

%automagic

2 ** 27
_
foo = 'bar'
foo
_i5

%logstart
%logstop
%logoff
output = !cmd
output

def main():
    x = 6
    y = 7.5
    result = x + y
#이프로그램을 ipython에서 실행한다면
if __name__ == '__main__':
    main()

class Message():
    def __init__(self, msg):
        self.msg = msg

    def __repr__(self):
        return ('Message: %s' % self.msg)

x = Message("I have a secret")
x
