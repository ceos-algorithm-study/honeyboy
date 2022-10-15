# https://www.acmicpc.net/problem/14888

import sys
from itertools import permutations

sys.stdin = open(
    '/Users/daeheon_macbook/Documents/Development/Python - Algo/Nadongbin/honeyboy/CH13-DFS-BFS/q19.txt', 'r')

while True:
    try:
        def doCalc(depth, add, min, mul, div, numbers, maxDepth, root, res):
            if (depth == maxDepth):
                res.append(root)
            if (add):
                add -= 1
                doCalc(depth + 1, add, min, mul, div, numbers,
                       maxDepth, root + numbers[depth], res)
                add += 1
            if (min):
                min -= 1
                doCalc(depth + 1, add, min, mul, div, numbers,
                       maxDepth, root - numbers[depth], res)
                min += 1
            if (mul):
                mul -= 1
                doCalc(depth + 1, add, min, mul, div, numbers,
                       maxDepth, root * numbers[depth], res)
                mul += 1
            if (div):
                div -= 1
                doCalc(depth + 1, add, min, mul, div, numbers, maxDepth,
                       int(root / numbers[depth]), res)
                div += 1

        n = int(input())
        numbers = list(map(int, input().split()))
        opers = list(map(int, input().split()))
        res = []

        doCalc(1, opers[0], opers[1], opers[2],
               opers[3], numbers, n, numbers[0], res)
        print(max(res))
        print(min(res))

        print("process finished")
    except EOFError:
        break
