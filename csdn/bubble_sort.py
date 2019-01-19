#!/usr/bin/env python
#-*- coding: utf-8 -*-

import random

def bubble_sort(seq):
    n = len(seq)
    for i in range(n-1):
        print(seq)
        for j in range(n-1-i):
            if seq[j] > seq[j+1]:
                seq[j], seq[j+1] = seq[j+1], seq[j]
        print(seq)

def test_bubble_sort():
    seq = list(range(10))
    random.shuffle(seq)
    sorted_seq = sorted(seq)
    bubble_sort(seq)
    assert seq == sorted_seq
