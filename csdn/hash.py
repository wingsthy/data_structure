#!/usr/bin/env python
#-*- coding: utf-8 -*-

class Array(object):

    def __init__(self, size=32, init=None):
        self._size = size
        self._items = [init] * size

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def __len__(self):
        return self._size

    def clear(self, value=None):
        for i in range(len(self._items)):
            self._items[i] = value

    def __iter__(self):
        for item in self._items:
            yield item

class Slot(object):
    def __init__(self, key, value):
        self.key, self.value = key, value

class HashTable(object):

    UNUSED = None  # 没被使用过
    EMPTY = Slot(None, None)  # 使用却被删除过

    def __init__(self):
        self._table = Array(8, init=HashTable.UNUSED)   # 保持 2*i 次方
        self.length = 0
