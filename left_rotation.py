# coding: utf-8

'''
@version: 0.1
@author: winxos
@license: MIT
@file: left_rotation.py
@created: 2016-11-24 12:29
'''

s=str(input()).split()
n,d=int(s[0]),int(s[1])
dd=str(input()).split()
buf=dd[d:]
buf+=dd[0:d]
print(" ".join(buf))
