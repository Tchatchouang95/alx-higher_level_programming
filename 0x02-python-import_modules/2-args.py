#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    num = len(argv) - 1
    if num < 1:
        print("{} arguments.".format(num))
    elif num == 1:
        print("{} argument:".format(num))
    else:
        print("{} arguments:".format(num))
    for x in range(num):
        print("{}: {}".format(x + 1, argv[x + 1]))
