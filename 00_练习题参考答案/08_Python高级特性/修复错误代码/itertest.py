#!/usr/bin/env python3

testlist = ['Linux', 'Java', 'Python', 'DevOps', 'Go']

it = iter(testlist)
print("Loop Start...")
while True:
    try:
        course = next(it)
        print(course)
    except StopIteration:
        print("Loop End")
        exit()
