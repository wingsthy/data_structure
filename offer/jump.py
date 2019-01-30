#!/usr/bin/env python
#-*- coding: utf-8 -*-

def jumpFloor(number):
    if number == 1 or number == 2:
        return number
    n, m = 1, 2
    for i in range(3,number+1):
        res = m + n
        n, m = m, res
    return res
if __name__ == '__main__':
    print(jumpFloor(10))
