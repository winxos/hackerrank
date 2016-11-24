# coding: utf-8

'''
@version: 0.1
@author: winxos
@license: MIT
@file: time_conversion.py
@created: 2016-11-24 14:27
'''

time = input().strip()
t1=time[2:-2]
t2=int(time[:2])
if time[-2:-1]=="P":
    t2+=12
    if t2==24:t2-=12
else:
    t2%=12
print("%02d%s"%(t2,t1))