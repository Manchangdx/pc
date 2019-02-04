import sys

a, b = [], []
for i in sys.argv[1:]:
    if len(i) > 3:
        b.append(i)
    else:
        a.append(i)

print(' '.join(a))
print(' '.join(b))
