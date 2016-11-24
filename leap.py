# coding: utf-8

'''
@version: 0.1
@author: winxos
@license: MIT
@file: leap.py
@created: 2016-11-24 13:00
'''
def leap(y):
    return y%400==0 or (y%100!=0 and y%4==0)
if __name__ == '__main__':
    pass