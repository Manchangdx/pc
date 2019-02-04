import sys

a = int(sys.argv[1])
if 0 <= a < 10:
    print('you belong to kids')
elif a < 18:
    print('you belong to teenager')
elif a < 30:
    print('you belong to adult')
elif a < 60:
    print('you belong to older')
elif a < 120:
    print('you belong to oldest')
