# coding: utf-8

'''
@version: 0.1
@author: winxos
@license: MIT
@file: multiples35.py
@created: 2016-11-24 14:47
'''

def f(n,a):
    m=n//a
    return (1+m)*m*a//2
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(f(n-1,3)+f(n-1,5)-f(n-1,15))