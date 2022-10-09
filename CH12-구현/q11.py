# 다음의 링크에서 풀이한다 https://www.acmicpc.net/problem/3190

import sys
from collections import deque

sys.stdin = open(
    '/Users/daeheon_macbook/Documents/Development/Python - Algo/Nadongbin/honeyboy/CH12-구현/q11.txt', 'r')


class Apple:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Turn:
    def __init__(self, time, dir):
        self.time = time
        self.dir = dir


class SnakeBody:
    def __init__(self, x, y):
        self.x = x
        self.y = y


directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]


def checkApple(appleList, snakeHead):
    for i in range(0, len(appleList)):
        if ((appleList[i].x == snakeHead.x) and (appleList[i].y == snakeHead.y)):
            del appleList[i]
            return True
    return False


def updateDir(turnList, currentDir):
    if (turnList[0].dir == "D"):
        currentDir += 1
    elif (turnList[0].dir == "L"):
        currentDir -= 1
    if (currentDir < 0):
        currentDir = 3
    elif (currentDir > 3):
        currentDir = 0
    return currentDir


def checkBodyCollision(snakeList, newBody):
    for body in snakeList:
        if (body.x == newBody.x and body.y == newBody.y):
            return True
    return False


while True:
    try:
        appleList = deque([])
        turnList = deque([])
        snakeList = deque([])
        timeSpent = 0
        currentDir = 0

        # handling input

        boardSize = int(input())
        appleCount = int(input())

        for i in range(0, appleCount):
            [column, row] = list(map(int, input().split()))
            appleList.append(Apple(row-1, column-1))

        turnCount = int(input())

        for i in range(0, turnCount):
            [period, dir] = input().split()
            turnList.append(Turn(int(period)+1, dir))

        snakeList.append(SnakeBody(0, 0))

        while True:
            timeSpent += 1

            # add new head
            if (turnList and turnList[0].time == timeSpent):
                currentDir = updateDir(turnList, currentDir)
                turnList.popleft()

            [x, y] = directions[currentDir]
            newBody = SnakeBody(snakeList[0].x + x, snakeList[0].y + y)

            # wall collision check
            if (newBody.x >= boardSize or newBody.x < 0):
                break
            elif (newBody.y >= boardSize or newBody.y < 0):
                break

            # body collision check
            if (checkBodyCollision(snakeList, newBody)):
                break

            # body modification
            if not (checkApple(appleList, snakeList[0])):
                snakeList.pop()
            snakeList.appendleft(newBody)

        print(timeSpent)

    except EOFError:
        print("process finished")
        break
