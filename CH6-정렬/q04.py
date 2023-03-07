from array import array
from re import L
import sys
from collections import deque

sys.stdin = open(
    '/Users/daeheon_macbook/Documents/Development/Python - Algo/Nadongbin/honeyboy/CH6-정렬/q04.txt', 'r')


while True:
    try:
        [arrayLen, maxCount] = list(map(int, input().split(' ')))
        origin = list(map(int, input().split(' ')))
        target = list(map(int, input().split(' ')))
        origin = sorted(origin)
        target = sorted(target, reverse=True)
        res = sum(origin[maxCount:]) + sum(target[:maxCount])
        print(res)
        break
    except EOFError:
        print("process finished")
        break

input_data = sys.stdin.readline().rstrip()
