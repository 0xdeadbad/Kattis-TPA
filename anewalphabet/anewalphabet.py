#!/usr/bin/env python3
"""
Autor: Matheus da Silva Garcias
Matrícula: 20171BSI0456
Problema: https://open.kattis.com/problems/anewalphabet
Resultado: https://open.kattis.com/submissions/5468063
"""

from sys import stdin, stdout

input = stdin.readline
print = stdout.write

symbols = ['@', '8', '(', '|)', '3', '#', '6', '[-]', '|', '_|', '|<', '1', r'[]\/[]', '[]\[]', '0', '|D', '(,)', '|Z', '$', '\'][\'', '|_|', r'\/', r'\/\/', '}{', '`/', '2']

t = input().lower()

for l in t:
    if ord(l) >= 97 and ord(l) <= 122:
        print(symbols[ord(l) - 97])
    else:
        print(l)

print('\n')