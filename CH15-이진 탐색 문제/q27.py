from re import L
import sys
from bisect import bisect_left, bisect_right

sys.stdin = open(
    '/Users/daeheon_macbook/Documents/Development/Python - Algo/Nadongbin/honeyboy/CH15-이진 탐색 문제/q27.txt', 'r')

while True:
    try:
        count, target = list(map(int, input().split(' ')))
        targetList = list(map(int, input().split(' ')))
        res = bisect_right(targetList, target) - \
            bisect_left(targetList, target)
        if (res):
            print(res)
        else:
            print("-1")

    except EOFError:
        print("process finished")
        break
