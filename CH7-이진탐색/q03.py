from re import L
import sys
from collections import deque

sys.stdin = open(
    '/Users/daeheon_macbook/Documents/Development/Python - Algo/Nadongbin/honeyboy/CH7-이진탐색/q03.txt', 'r')

while True:
    try:
        count, requirement = list(map(int, input().split(' ')))
        riceCakes = list(map(int, input().split(' ')))
        start = 0
        end = max(riceCakes)
        prevRes = -1
        while (end > start):
            # cutter의 길이를 업데이트 합니다
            res = 0
            cutter = (end + start) // 2
            # 모든 떡에 대해서 결과를 구합니다
            for cake in riceCakes:
                if ((cake - cutter) > 0):
                    res += (cake - cutter)
            # 이전 실행의 결과와 비교합니다
            if (prevRes != -1 and res > prevRes):
                break
            else:
                prevRes = res
            # 결과를 토대로 start, end 값을 업데이트 합니다
            if (res > requirement):
                start = cutter
            elif (res < requirement):
                end = cutter
            else:
                break
        print(cutter)
    except EOFError:
        print("process finished")
        break
