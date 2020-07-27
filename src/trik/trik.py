#!/usr/bin/env python3
"""
Autor: Matheus da Silva Garcias
Matrícula: 20171BSI0456
Problema: https://open.kattis.com/problems/trik
Resultado: https://open.kattis.com/submissions/5892564
"""

from sys import stdin, stdout

input = stdin.readline
print = stdout.write

state = [1, 0, 0]

line = input()

for l in line:
    if l == 'A':
        state[0], state[1] = state[1], state[0]
    elif l == 'B':
        state[1], state[2] = state[2], state[1]
    elif l == 'C':
        state[0], state[2] = state[2], state[0]

for i in range(3):
    if state[i]:
        print(str(i+1)+'\n')
        break