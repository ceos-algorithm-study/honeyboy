import sys
from itertools import combinations

sys.stdin = open(
    '/Users/daeheon_macbook/Documents/Development/Python - Algo/Nadongbin/honeyboy/CH12-구현/q13.txt', 'r')


def getCityDist(houseList, chickenList):

    distSum = 0
    for house in houseList:
        minDist = -1
        for chicken in chickenList:
            curDist = abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])
            if (minDist < 0):
                minDist = curDist
            else:
                minDist = min(minDist, curDist)
        distSum += minDist
    return distSum


while True:
    try:
        gridSize, maxNum = list(map(int, input().split()))
        tempList = []
        houseList = []
        chickenList = []

        for y in range(0, gridSize):
            tempList = list(map(int, input().split()))
            for x, item in enumerate(tempList):
                if (item == 1):
                    houseList.append([x, y])
                elif (item == 2):
                    chickenList.append([x, y])

        chickenCases = combinations(chickenList, maxNum)

        candidates = []

        for case in chickenCases:
            candidates.append(getCityDist(houseList, case))

        print(min(candidates))

    except EOFError:
        print("process finished")
        break
