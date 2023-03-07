# https://www.acmicpc.net/problem/10825

from re import L
import sys
from collections import deque

sys.stdin = open(
    '/Users/daeheon_macbook/Documents/Development/Python - Algo/Nadongbin/honeyboy/CH14-정렬/q23.txt', 'r')

while True:
    try:
        cnt = int(input())
        namebook = [[] for _ in range(cnt)]
        for i in range(cnt):
            temp = input().split(' ')
            namebook[i].append(temp[0])
            namebook[i].extend(map(int, temp[1:]))
        namebook = sorted(namebook, key=lambda item: item[0])
        namebook = sorted(namebook, key=lambda item: item[3], reverse=True)
        namebook = sorted(namebook, key=lambda item: item[2], reverse=False)
        namebook = sorted(namebook, key=lambda item: item[1], reverse=True)
        for name in namebook:
            print(name[0])

    except EOFError:
        print("process finished")
        break
