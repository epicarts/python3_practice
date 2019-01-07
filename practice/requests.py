
for i in range(128):
    res = requests.get(f'http://www.randomtext.me/api/lorem/p-1/32')
    with open(f'{i}.txt', 'w') as f:
        f.write(res.text)
