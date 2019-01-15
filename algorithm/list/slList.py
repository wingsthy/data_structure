#!/usr/bin/env python
#-*- coding: utf-8 -*-
#单向循环链表

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class CircularLinkedListOneway(object):
    def __init__(self, node=None):
        if node:
            node.next = node
        self.__head = node

    def is_empty(self):
        return self.__head == None

    def __len__(self):
        count = 1
        cur = self.__head
        if self.is_empty():
            return 0
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return count

    def traversal(self):
        if self.is_empty():
            return
        cur = self.__head
        while cur.next != self.__head:
            print(cur.value)
            cur = cur.next
        print(cur.value)

    def add(self, value):
        node = Node(value)
        if self.is_empty():
            self.__head = node
            self.__head.next = self.__head
            return
        cur = self.__head
        while cur.next != self.__head:
            cur = cur.next
        node.next = self.__head
        self.__head = node
        cur.next = self.__head

    def append(self, value):
        node = Node(value)
        cur = self.__head
        if self.is_empty():
            self.__head = node
            self.__head.next = self.__head
            return
        while cur.next != self.__head:
            cur = cur.next
        node.next = cur.next
        cur.next = node

    def insert(self, pos, value):
        if pos <= 0:
            self.add(value)
        elif pos > len(self) - 1:
            self.append(value)
        else:
            node = Node(value)
            cur = self.__head
            count = 0
            while count < pos - 1:
                count += 1
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def search(self, value):
        if self.is_empty():
            return False
        cur = self.__head
        while cur.next != self.__head:
            if cur.value == value:
                return True
            else:
                cur = cur.next
        if cur.value == value:
            return True
        return False

    def remove(self, value):
        cur = self.__head
        prior = None
        if self.is_empty():
            return
        while cur.next != self.__head:
            if cur.value == value:
                if cur == self.__head:
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next
                    self.__head = cur.next
                    rear.next = self.__head
                else:
                    prior.next = cur.next
                return
            else:
                prior = cur
                cur = cur.next
        if cur.value == value:
            if cur == self.__head:
                self.__head = None
                return
            prior.next = cur.next
