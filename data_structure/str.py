#!/usr/bin/env python
#-*- coding: utf-8 -*-
#字符串匹配

def stringCompare(str1, str2):
    if str1 in str2:
        print("yes1")


def stringCompare2(str1, str2):
    if str1.index(str2) > -1:
        print("yes2")


def stringCompare3(str1, str2):
    if str1.find(str2) > -1:
        print("yes3")


if __name__ == '__main__':
    a = "helloworld"
    b = "world"
    stringCompare(b, a)
    stringCompare2(a, b)
    stringCompare3(a, b)

