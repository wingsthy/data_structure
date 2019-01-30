#!/usr/bin/env python
#-*- coding: utf-8 -*-

def btjumpFloor(number):
    ans=[]
    ans.append(0)
    ans.append(1)
    ans.append(2)
    for i in range(3, number+1):
        sum = 1
        for j in range(1, i):
            sum += ans[j]
        ans.append(sum)
    return ans[number]

if __name__ == '__main__':
    print(btjumpFloor(10))
