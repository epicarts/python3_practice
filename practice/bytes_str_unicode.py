'''
아래 3개의 차이점!!
1. bytes 파이썬 3
2. str 파이썬 3,2
3. unicode 파이썬 2
'''
#파이썬 3에서
#입력: str, bytes => 아웃풋: str
def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value #str 인스턴스

#입력 str, bytes => 아웃풋: bytes
def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value # bytes 인스턴스

#파이썬 2도 마찬가지로 str 이나 unicode를 입력
