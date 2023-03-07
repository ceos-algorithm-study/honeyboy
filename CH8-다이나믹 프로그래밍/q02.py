from re import L
import sys
from collections import deque

sys.stdin = open(
    '/Users/daeheon_macbook/Documents/Development/Python - Algo/Nadongbin/honeyboy/CH8-다이나믹 프로그래밍/q02.txt', 'r')

while True:
    try:
        inputValue = int(input())
        dp = [0 for _ in range(inputValue + 1)]
        dp[1] = 1
        for i in range(2, inputValue + 1):
            cands = []
            if (dp[i-1]):
                cands.append(dp[i-1] + 1)
            if (i % 2 == 0 and dp[i//2]):
                cands.append(dp[i//2] + 1)
            if (i >= 3 and i % 3 == 0 and dp[i//3]):
                cands.append(dp[i//3] + 1)
            if (i >= 5 and i % 5 == 0 and dp[i//5]):
                cands.append(dp[i//5] + 1)
            if (cands):
                dp[i] = min(cands)
        print(dp[inputValue] - 1)

    except EOFError:
        print("process finished")
        break
