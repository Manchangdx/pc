import sys

d = {}
for i in sys.argv[1:]:
    a, b = i.split(':')
    d[a] = b

for key, value in d.items():
    print('ID:{} Name:{}'.format(key, value))
