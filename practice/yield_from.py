@asnycio.coroutine
def coro():
    yield from asyncio.sleep(1)
    print('Hello world!')


def gen1():
    for x in range(10):
        yield x
    for x in range(5):
        yield x


def gen2():
    yield from range(10)
    yield from range(5)


for a, b in zip(gen1(), gen2()):
    assert a == b
