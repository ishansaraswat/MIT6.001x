# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 01:54:39 2018

@author: ishan
"""
s = 'azcbobobegghakl'
num_vowels = 0
for letter in s:
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        num_vowels += 1
print('Number of vowels:', num_vowels)