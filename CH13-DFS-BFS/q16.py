# https://www.acmicpc.net/problem/14502

from distutils.command.build import build
import sys
import copy
import itertools

sys.stdin = open(
    '/Users/daeheon_macbook/Documents/Development/Python - Algo/Nadongbin/honeyboy/CH13-DFS-BFS/q16.txt', 'r')


while True:
    try:
        def contaminate():
            virusList = copy.deepcopy(inputVirusList)
            lab_test = copy.deepcopy(lab)
            while virusList:
                y, x = virusList.pop()

                for i in range(4):
                    ny = y + directionList[i][0]
                    nx = x + directionList[i][1]

                    if ((0 <= nx < xb) and (0 <= ny < yb)):
                        if (lab_test[ny][nx] == 0):
                            lab_test[ny][nx] = 2
                            virusList.append((ny, nx))

            safeZone = sum(i.count(0) for i in lab_test)
            global answer
            answer = max(answer, safeZone)

        def buildWall():
            wallSet = itertools.combinations(inputSpaceList, 3)
            for walls in wallSet:
                lab[walls[0][0]][walls[0][1]] = 1
                lab[walls[1][0]][walls[1][1]] = 1
                lab[walls[2][0]][walls[2][1]] = 1
                contaminate()
                lab[walls[0][0]][walls[0][1]] = 0
                lab[walls[1][0]][walls[1][1]] = 0
                lab[walls[2][0]][walls[2][1]] = 0

        lab = []
        temp = []
        inputVirusList = []
        inputSpaceList = []
        directionList = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        answer = 0

        yb, xb = map(int, input().split())
        for j in range(yb):
            temp = list(map(int, input().split()))
            lab.append(temp)
            for i in range(xb):
                if (temp[i] == 2):
                    inputVirusList.append((j, i))
                elif (temp[i] == 0):
                    inputSpaceList.append((j, i))

        buildWall()
        print(answer)

    except EOFError:
        print("process finished")
        break
