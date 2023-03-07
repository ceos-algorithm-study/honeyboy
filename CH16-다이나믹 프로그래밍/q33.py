# https://www.acmicpc.net/problem/14501

from re import L
import sys

sys.stdin = open(
    '/Users/daeheon_macbook/Documents/Development/Python - Algo/Nadongbin/honeyboy/CH16-다이나믹 프로그래밍/q33.txt', 'r')

while True:
    try:
        dateList = []
        candList = []
        dateCnt = int(input())
        for d in range(dateCnt):
            dateList.append(list(map(int, input().split())))
            dateList[d].append([0])

        for d in range(dateCnt):
            if (d + dateList[d][0] < dateCnt):
                for c in range(d + dateList[d][0], dateCnt):
                    dateList[c][2].append(max(dateList[d][2]) + dateList[d][1])
                # dateList[d + dateList[d][0]
                #          ][2].append(max(dateList[d][2]) + dateList[d][1])
            elif (d + dateList[d][0] == dateCnt):
                candList.append(max(dateList[d][2]) + dateList[d][1])
            else:
                candList.append(max(dateList[d][2]))

        print(max(candList))

    except EOFError:
        print("process finished")
        break
