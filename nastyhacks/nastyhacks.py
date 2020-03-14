#!/usr/bin/env python3

from sys import stdin, stdout

input = stdin.readline
print = stdout.write

n = int(input())

for i in range(n):
    r, e, c = [int(x) for x in input().strip().split(' ')]
    print("does not matter\n" if r + c == e else "do not advertise\n" if r + c > e else "advertise\n")