# coding: utf-8

'''
@version: 0.1
@author: winxos
@license: MIT
@file: test.py
@created: 2016-11-24 15:08
'''
a0,a1,a2 = input().strip().split(' ')
a0,a1,a2 = [int(a0),int(a1),int(a2)]
b0,b1,b2 = input().strip().split(' ')
b0,b1,b2 = [int(b0),int(b1),int(b2)]
print("%d %d"%(int(a0>b0)+int(a1>b1)+int(a2>b2),int(b0>a0)+int(b1>a1)+int(b2>a1)))