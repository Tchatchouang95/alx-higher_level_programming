#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    num = len(argv) - 1
    sum = 0
    if num < 1:
        print("{:d}".format(0))
    else:
        for i in range(num):
            sum += int(argv[i + 1])
        print("{:d}".format(sum))
