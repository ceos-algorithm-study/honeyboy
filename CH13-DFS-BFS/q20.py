# https://www.acmicpc.net/problem/18428
import sys
from itertools import combinations
from copy import deepcopy

sys.stdin = open(
    '/Users/daeheon_macbook/Documents/Development/Python - Algo/Nadongbin/honeyboy/CH13-DFS-BFS/q20.txt', 'r')

while True:
    try:
        hallway = []
        emptySet = []
        teacherSet = []
        direction = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        flag = True

        def dig(teacher, tempHallway, direction, n):
            for item in direction:
                ay = teacher[1] + item[1]
                ax = teacher[0] + item[0]
                while (0 <= ax < n and 0 <= ay < n):
                    if (tempHallway[ay][ax] == "B"):
                        break
                    elif (tempHallway[ay][ax] == "S"):
                        return False
                    ay += item[1]
                    ax += item[0]
            return True

        # 값을 입력받는다
        n = int(input())

        for y in range(n):
            hallway.append(input().split())
            for x, item in enumerate(hallway[y]):
                if (item == "X"):
                    emptySet.append((x, y))
                elif (item == "T"):
                    teacherSet.append((x, y))

        # 벽을 놓는 방법에 대한 조합을 생성한다
        wallSet = combinations(emptySet, 3)
        res = True

        for walls in wallSet:
            tempHallway = deepcopy(hallway)
            res = True
            for wall in walls:
                tempHallway[wall[1]][wall[0]] = "B"
            for teacher in teacherSet:
                res = dig(teacher, tempHallway, direction, n)
                if (res == False):
                    break
            if (res == True):
                break

        if (res):
            print("YES")
        else:
            print("NO")

        print("process finished")
    except EOFError:
        break
