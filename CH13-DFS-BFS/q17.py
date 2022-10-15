# acmicpc.net/problem/18405
import sys
from collections import deque
from copy import deepcopy


sys.stdin = open(
    '/Users/daeheon_macbook/Documents/Development/Python - Algo/Nadongbin/honeyboy/CH13-DFS-BFS/q17.txt', 'r')


def updateValue(id, x, y, tube, tubeSize, virusList):
    if (x > 0 and (tube[x - 1][y] == 0)):
        tube[x - 1][y] = id
        virusList.append([id, x - 1, y])
    if (y > 0 and (tube[x][y - 1] == 0)):
        tube[x][y - 1] = id
        virusList.append([id, x, y - 1])
    if (x < tubeSize - 1 and (tube[x + 1][y] == 0)):
        tube[x + 1][y] = id
        virusList.append([id, x + 1, y])
    if (y < tubeSize - 1 and (tube[x][y + 1] == 0)):
        tube[x][y + 1] = id
        virusList.append([id, x, y + 1])
    virusList.popleft()


while True:
    try:
        [tubeSize, virusCnt] = list(map(int, input().split()))
        tube = []
        temp = []
        virusList = deque([])

        for x in range(tubeSize):
            temp = list(map(int, input().split()))
            tube.append(temp)
            for y, item in enumerate(temp):
                if (item > 0):
                    virusList.append([item, x, y])
        sorted(virusList, key=lambda x: x[0])

        [second, x, y] = list(map(int, input().split()))

        for i in range(second):
            virusIter = deepcopy(list(virusList))
            for virus in virusIter:
                updateValue(virus[0], virus[1], virus[2],
                            tube, tubeSize, virusList)

        for i in tube:
            print(i)

        print(tube[x - 1][y - 1])

    except EOFError:
        print("process finished")
        break


# from collections import deque
# from copy import deepcopy

# def updateValue(id, x, y, tube, tubeSize, virusList):
#     if (x > 0 and (tube[y][x - 1] == 0)):
#         tube[y][x - 1] = id
#         virusList.append([id, x - 1, y])
#     if (y > 0 and (tube[y - 1][x] == 0)):
#         tube[y - 1][x] = id
#         virusList.append([id, x, y - 1])
#     if (x < tubeSize - 1 and (tube[y][x + 1] == 0)):
#         tube[y][x + 1] = id
#         virusList.append([id, x + 1, y])
#     if (y < tubeSize - 1 and (tube[y + 1][x] == 0)):
#         tube[y + 1][x] = id
#         virusList.append([id, x, y + 1])
#     virusList.popleft()

# [tubeSize, virusCnt] = list(map(int, input().split()))
# tube = []
# temp = []
# virusList = deque([])

# for row in range(tubeSize):
#     temp = list(map(int, input().split()))
#     tube.append(temp)
#     for col, item in enumerate(temp):
#         if (item > 0):
#             virusList.append([item, col, row])
# sorted(virusList, key=lambda x: x[0])

# [second, y, x] = list(map(int, input().split()))

# for i in range(second):
#     virusIter = deepcopy(list(virusList))
#     for virus in virusIter:
#         updateValue(virus[0], virus[1], virus[2],
#                     tube, tubeSize, virusList)

# print(tube[y - 1][x - 1])
