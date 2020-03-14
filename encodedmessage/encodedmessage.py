#!/usr/bin/env python3
"""
Autor: Matheus da Silva Garcias
Matrícula: 20171BSI0456
Problema: https://open.kattis.com/problems/encodedmessage
Resultado: https://open.kattis.com/submissions/5464102
"""

from sys import stdin, stdout
from math import sqrt

input = stdin.readline
print = stdout.write

n = int(input())

for _ in range(n):
    m = input()
    s = int(sqrt(len(m)))
    for j in range(s, 0, -1):
        for i in range(s):
            print(m[i*s+j-1])
    print("\n")
