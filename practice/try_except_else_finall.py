'''
try/finally: 예외를 전달하고 싶지만 예외가 발생해도 실행하고 싶을떄
'''

#이코드에서는 파일 핸들을 read 할
handle = open('/tmp/random_data.txt')# IO에러 가능성이 있음
try:
    data = handle.read()#유티코드 디코드 에러가 일어날 수 있음.
finally:
    handle.close()#try: 이후에 항상 실행됨

'''
try/except/else 블록: 어떤 예외를 전달할지 명확하게 처리
else 블록을 사용하면 try 블록의 코드를 최소로 줄일수 잇음
중요: 함수 내부에서 일어나는 에러냐, 함수 외부에서 일어나는 에러냐를
except을 사용하여 정확하게 호출되는 부분을 정해야함.

'''

def load_json_key(data, key):
    try:
        result_dict = json.loads(data)#valueError 이 일어날 수 있음
    except ValueError as e:#올바른 JSON이 아니라면 값 에러가 일어남.
        raise KeyError from e
    else:
        #디코딩이 성공하면 else 블록에서 키를 찾음.
        #만약 여기서 에러가 발생하면 함수 밖으로 예외 전달행위를 명확하게 함
        return result_dict[key]

'''
다함께 사용!!
파일 수행할 작업 read => 처리 => 파일 업데이트
'''
UNDEFINED = object()
UNDEFINED
type(UNDEFINED)

def divide_json(path):
    handle = open(path, 'r+')#IO 에러가 일어날 수 있음
    try:#파일핸들을 읽고 처리함.
        data = handle.read()#UnicodeDecodeError
        op = json.loads(data)#ValueError
        value = (
            op['numerator'] /
            op['denominator']) #ZeroDivisionError
    except ZeroDivisionError as e:
        return UNDEFINED
    #try 블록이 예외를 발생하지 않으면 else 가 실행됨.
    else:# 파일을 즉석에서 업데이트하고 이와 관련한 예외가 전달되게 하는데 사용
        op['result'] = value#try에서 만든 value를 이용하여 dump를 만듬.
        result = json.dumps(op)#
        handle.seek(0)
        handle.write(result)# IO Error이 일어날 수 있음
        return value
    finally:
        handle.close() # 항상 실행함/ 파일을 닫아야 하므로 항상!!실행함
