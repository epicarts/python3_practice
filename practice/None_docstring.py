'''
키워드 인수의 기본값으로 비정적(non-static) 타입 사용.
ex)함수가 호출 된 시간을 메시지에 포함하고 싶다.

None를 사용하는 것은 인수가 수정(mutalbe) 가능 할때 중요함.
ex) JSON 데이터로 인코드된 값을 로드 할대

결론: 기본 인수는 모듈 로드 시점에서 함수 정의 과정에서 딱 한번만 평가됨.
그니까 {} 와 [] 같은 동적 값에는 이상하게 동작하는 원인이 되기도함
그래서 동적 값 키워드 인수에는 기본값으로 None 을 놓고 docstring 에 기본 동작 문서를
문서화 하쟈!!

'''

import datetime
from time import sleep
import json

def log(message, when=datetime.datetime.now()):
    print('%s: %s' % (when, message))

#딱 한번만 실행되므로 타임스탬프가 동일하게 출력됨.
log('Hi~~')
log('Hi~~')

def log2(message, when=None):#when 을 None으로 놓고 문서화로 실제 동작을 문서화.
    """Log a message with a timestamp

    Arts:
        message: Message to printself.
        when: datatime of when the message occurred
            Defaults to the present time
    """
    when = datetime.datetime.now() if when is None else when
    print('%s: %s' % (when, message))

log2('Hi~~')
log2('Hi~~')


#이 함수 또한 기본 인수 값은 모듈이 로드 될떄 딱 한번만 평가 실행되므로
#기본값으로 설정한 딕셔너리를 모든 decode 호출에서 공유함.
def decode(data, default={}):
    try:
        return json.loads(data)
    except ValueError:
        return default

foo = decode('bad data')
foo['stuff'] = 5
bar = decode('also bad')
bar['meep'] = 1
print('Foo:', foo)
print('Bar:', bar)

#둘 다 기본 파라미터가 같다. 즉, 같은 딕셔너리 객체이다
assert foo is bar

def decode2(data, default=None):
    """Load JSON data from a string.

    Args:
        data: JSON data to decode.
        default: Value to return if decoding fails.
            Defaults to an empty dictionary.
    """
    if default is None:
        default = {}
    try:
        return json.loads(data)
    except ValueError:
        return default

foo = decode2('bad data')
foo['stuff'] = 5
bar = decode2('also bad')
bar['meep'] = 1
print('Foo:', foo)
print('Bar:', bar)
