#!/usr/bin/env python3
"""
Autor: Matheus da Silva Garcias
Matrícula: 20171BSI0456
Problema: https://open.kattis.com/problems/nastyhacks
Resultado: https://open.kattis.com/submissions/5463684
"""

from sys import stdin, stdout

input = stdin.readline
print = stdout.write

n = int(input())

for _ in range(n):
    r, e, c = [int(x) for x in input().strip().split(' ')]
    print("does not matter\n" if r + c == e else "do not advertise\n" if r + c > e else "advertise\n")