#!/usr/bin/env python3
"""
Autor: Matheus da Silva Garcias
Matrícula: 20171BSI0456
Problema: https://open.kattis.com/problems/oddgnome
Resultado: https://open.kattis.com/submissions/5464256
"""

from sys import stdin, stdout
from math import sqrt

input = stdin.readline
print = stdout.write

n = int(input())

for _ in range(n):
    g = [int(x) for x in input().strip().split(' ')][1:]
    for i in range(1, len(g)):
        if g[i] - g[i-1] != 1:
            print(str(i+1)+'\n')
            break