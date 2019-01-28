# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 02:07:54 2018

@author: ishan
"""
s = 'azcbobobegghakl'
count = 0
check = 'bob'
for iters in range(len(s)-2):
    if s[iters:iters+3] == check:
        count += 1
print('Number of times bob occurs is:', count)
