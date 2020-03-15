#!/usr/bin/env python3
"""
Autor: Matheus da Silva Garcias
Matrícula: 20171BSI0456
Problema: https://open.kattis.com/problems/brokenswords
Resultado: https://open.kattis.com/submissions/5467655
"""

from sys import stdin, stdout

input = stdin.readline
print = stdout.write

tb, lr = (0, 0)
q = 0

n = int(input())

for _ in range(n):
    s = int(input(), 2)
    tb += (((s >> 2) & 1) ^ 1) + ((s >> 3) ^ 1)
    lr += (((s & 0b0010) >> 1) ^ 1) + ((s & 1) ^ 1)

while(tb >= 2 and lr >= 2):
    q += 1
    tb -= 2
    lr -= 2

print("%d %d %d\n" % (q, tb, lr))