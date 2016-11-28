# coding: utf-8
n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
c = input().strip().split(' ')
c = [int(i) for i in c]
c = sorted(c)

cache = {}


def dycoin(rest, max_c):
    if rest == 0: return 1
    if rest < 0: return 0
    if (rest,max_c) in cache:
        return cache[(rest,max_c)]
    sum = 0
    for i in c:
        if i > max_c: break
        sum += dycoin(rest - i, i)
    cache[(rest, max_c)] = sum
    return sum


print(dycoin(n, c[-1]))
