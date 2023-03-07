# https://www.acmicpc.net/problem/2110

from re import L
import sys

sys.stdin = open(
    '/Users/daeheon_macbook/Documents/Development/Python - Algo/Nadongbin/honeyboy/CH15-이진 탐색 문제/q29.txt', 'r')

while True:
    try:
        locations = []
        houseCnt, hubCnt = list(map(int, input().split()))
        locations = [[int(input().rstrip()) for _ in range(houseCnt)]]
        # for i in range(houseCnt):
        #     locations.append(int(input()))
        locations.sort()

        start = 1
        end = locations[-1] - locations[0]
        answer = 0

        while (start <= end):
            mid = (start + end) // 2
            count = 1
            currentPos = locations[0]
            for i in range(1, len(locations)):
                if (locations[i] >= currentPos + mid):
                    count += 1
                    currentPos = locations[i]
            if (count >= hubCnt):
                start = mid + 1
                answer = mid
            else:
                end = mid - 1

        print(answer)

    except EOFError:
        print("process finished")
        break
