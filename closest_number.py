# coding: utf-8

'''
@version: 0.1
@author: winxos
@license: MIT
@file: closest_number.py
@created: 2016-11-24 12:13
'''
def cn(a,b,x):
    c=a**b
    if c%x < x*0.5:
        return int(c//x*x)
    else:
        return int(c//x*x+x)
n = int(input())
for i in range(n):
    l = str(input())
    cs =[int(i) for i in l.split()]
    print(cn(cs[0],cs[1],cs[2]))