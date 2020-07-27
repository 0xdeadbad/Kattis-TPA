#!/usr/bin/env python3
"""
Autor: Matheus da Silva Garcias
Matrícula: 20171BSI0456
Problema: https://open.kattis.com/problems/apaxiaaans
Resultado: https://open.kattis.com/submissions/5892569
"""

from sys import stdin, stdout

input = stdin.readline
print = stdout.write

n = input()

if len(n) == 1:
    print(n + '\n')
else:
    last_letter = ''
    for l in n:
        if(l != last_letter):
            print(l)
            last_letter = l