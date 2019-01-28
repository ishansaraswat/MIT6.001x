# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 20:15:01 2018

@author: ishan
"""
s = 'xwyxsujytanx'

temp = s[0]
longest = ''

for i in range(len(s)-1):
    if s[i+1] >= s[i]:
        temp = temp + s[i+1]
    else:
        if len(temp) > len(longest):
            longest = temp
            temp = s[i+1]
        else:
            temp = s[i+1]
            
if len(temp) > len(longest):
    longest = temp
    
print('Longest substring in alphabetical order is:' + longest)