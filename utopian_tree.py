#!/bin/python3

import sys

def f(n):
    if n==0:return 1
    if n%2==0:return f(n-1)+1
    else:return f(n-1)*2
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(f(n))