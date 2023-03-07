# https://www.acmicpc.net/problem/18310

from re import L
import sys
from collections import deque

sys.stdin = open(
    '/Users/daeheon_macbook/Documents/Development/Python - Algo/Nadongbin/honeyboy/CH14-정렬/q24.txt', 'r')

while True:
    try:
        cnt = int(input())
        items = list(map(int, input().split(' ')))
        items = sorted(items)
        mid = cnt // 2
        if (cnt % 2 == 0):
            print(items[mid - 1])
        else:
            print(items[mid])
    except EOFError:
        print("process finished")
        break
