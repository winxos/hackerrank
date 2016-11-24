# coding:utf-8
# winxos 2016-11-24
buf = []


def interpreter(s: str):
    cmds = s.split()
    op = cmds[0]
    if op == "insert":
        buf.insert(int(cmds[1]), int(cmds[2]))
    if op == "print":
        print(buf)
    if op == "remove":
        buf.remove(int(cmds[1]))
    if op == "append":
        buf.append(int(cmds[1]))
    if op == "pop":
        buf.pop()
    if op == "sort":
        buf.sort()
    if op == "reverse":
        buf.reverse()


n = int(input())
for i in range(n):
    l = input()
    interpreter(l)
