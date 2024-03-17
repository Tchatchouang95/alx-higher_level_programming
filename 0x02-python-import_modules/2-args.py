#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
   num = len(argv) - 1
   if num < 0:
       print("{} arguments.".format(num))
   elif num == 1:
       print("{} argument:".format(num))
   else:
       print("{} arguments:".format(num))
   for x in range(num):
       print("{:d}: {}".format(x + 1, argv[x + 1]))
