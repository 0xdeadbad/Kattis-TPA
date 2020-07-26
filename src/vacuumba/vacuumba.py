#!/usr/bin/env python3
"""
Autor: Matheus da Silva Garcias
Matrícula: 20171BSI0456
Problema: https://open.kattis.com/problems/vacuumba
Resultado: https://open.kattis.com/submissions/5467802
"""

from sys import stdin, stdout
from math import cos, sin, radians

input = stdin.readline
print = stdout.write

n = int(input())

for _ in range(n):
    m = int(input())
    x, y, a = (float(0), float(0), float(90))
    for _ in range(m):
        na, d = [float(x) for x in input().strip().split(' ')]
        a += na
        x += cos(radians(a)) * d
        y += sin(radians(a)) * d
    print('%.6f %.6f\n' % (x, y))

