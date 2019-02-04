num = input("Enter number:")
try:
    new_num = int(num)
except ValueError:
    exit()
print('INT:{}'.format(new_num))
