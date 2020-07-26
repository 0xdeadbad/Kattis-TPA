#!/usr/bin/env python3
"""
Autor: Matheus da Silva Garcias
Matrícula: 20171BSI0456
Problema: https://open.kattis.com/problems/speedlimit
Resultado: https://open.kattis.com/submissions/5463805
"""

from sys import stdin, stdout

input = stdin.readline
print = stdout.write

n = int(input())

while(n > -1):
    miles = 0
    last_t = 0
    for _ in range(n):
        s, t = [int(x) for x in input().strip().split(' ')]
        tmp = t
        t -= last_t
        miles += t * s
        last_t = tmp
    print("%d miles\n" % miles)

    n = int(input())