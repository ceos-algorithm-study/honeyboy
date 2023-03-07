# https://www.acmicpc.net/problem/1715

from re import L
import sys
import heapq

sys.stdin = open(
    '/Users/daeheon_macbook/Documents/Development/Python - Algo/Nadongbin/honeyboy/CH14-정렬/q26.txt', 'r')

while True:
    try:
        heapList = []
        sum = 0
        cnt = int(input())
        for i in range(cnt):
            heapq.heappush(heapList, int(input()))

        while (len(heapList) != 1):
            one = heapq.heappop(heapList)
            two = heapq.heappop(heapList)
            sum_value = one + two
            sum += sum_value
            heapq.heappush(heapList, sum_value)
        print(sum)

    except EOFError:
        print("process finished")
        break
