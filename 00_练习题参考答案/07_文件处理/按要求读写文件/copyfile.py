with open('shiyanlou.txt') as f1:
    with open('shiyanlou_copy.txt', 'w') as f2:
        for n, w in enumerate(f1.readlines()):
            f2.write('{} {}'.format(n+1, w))
