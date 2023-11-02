#!/usr/bin/python3
for i in range(122, 96, -1):
    if i % 2 == 0:
        char = chr(i).lower()
    else:
        char = chr(i).upper()
    print("{}".format(char), end='')
