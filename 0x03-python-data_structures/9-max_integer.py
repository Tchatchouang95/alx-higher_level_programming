#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    else:
        max = my_list[0]
        size = len(my_list)
        for i in range(1, size):
            if my_list[i] > max:
                max = my_list[i]
        return max
