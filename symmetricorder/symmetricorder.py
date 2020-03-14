#!/usr/bin/env python3
"""
Autor: Matheus da Silva Garcias
Matrícula: 20171BSI0456
Problema: https://open.kattis.com/problems/symmetricorder
Resultado: https://open.kattis.com/submissions/5464202
"""

from sys import stdin, stdout
from math import sqrt

input = stdin.readline
print = stdout.write

n = int(input())
j = 1

while(n != 0):
    print("SET %d\n" % j)
    j += 1
    top = []
    bottom = []
    switch = True
    for _ in range(n):
        if switch:
            top.append(input())
        else:
            bottom.append(input())
        switch = not switch
    for string in top:
        print(string)
    for i in range(len(bottom)-1, -1, -1):
        print(bottom[i])

    n = int(input())