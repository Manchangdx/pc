def compute(base, value):
    base_cp = base[:]
    base_cp.append(value)
    print(sum(base_cp))

if __name__ == '__main__':
    testlist = [10, 20, 30]
    compute(testlist, 15)
    compute(testlist, 25)
    compute(testlist, 35)
