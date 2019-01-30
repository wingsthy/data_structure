#!/usr/bin/env python
#-*- coding: utf-8 -*-

# 使用两个栈实现一个队列
class Queue(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    #入队
    def enqueue(self,element):
        if self.stack1:
            self.stack1.append(element)
        else:
            while self.stack2:
                self.stack1.append(self.stack2.pop())
            self.stack1.append(element)

    #出队
    def dequeue (self):
        if self.stack2:
            return self.stack2.pop()
        elif self.stack1:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
        else:
            return None

if __name__=='__main__':
    queue = Queue()
    queue.enqueue('9')
    queue.enqueue('10')
    queue.enqueue('6')
    queue.enqueue('2')

    print queue.dequeue()
    print queue.dequeue()
    print queue.dequeue()
    print queue.dequeue()


