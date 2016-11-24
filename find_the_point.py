# coding: utf-8

'''
@version: 0.1
@author: winxos
@license: MIT
@file: find_the_point.py
@created: 2016-11-24 12:04
'''


def fp(x1, y1, x2, y2):
    return x2 * 2 - x1, y2 * 2 - y1


n = int(input())
for i in range(n):
    l = str(input())
    cs = l.split()
    x, y = fp(int(cs[0]), int(cs[1]), int(cs[2]), int(cs[3]))
    print(x, y)
