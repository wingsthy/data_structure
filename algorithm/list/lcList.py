#!/usr/bin/env python
#-*- coding: utf-8 -*-

class LCList: #循环单链表类
    def __init__(self):
        self._rear = None 

    def is_empty(self):
        return self._rear 

    def prepend(self, elem):
        p = LNode(elem)
        if self._rear is None:
            p.next = p
            self._rear = p
        else:
            p.next = self._rear.next 
            self._rear.next = p

    def append(self, elem):
        self.prepend(elem)
        self._rear = self._rear.next 

    def pop(self):
        if self._rear is None:
            raise LinkedListUnderflow("in pop of LCList")
        p = self._rear.next 
        if self._rear is p:
            self._rear = None 
        else:
            self._rear.next = p.next 
        return p.elem 

    def printall(self):
        if self.is_empty():
            return 
        p = self._rear.next 
        while True:
            print(p.elem)
            if p is self._rear:
                break 
            p = p.next 

