# https://www.acmicpc.net/problem/16234
import sys
from collections import deque
from copy import deepcopy
import math

sys.stdin = open(
    '/Users/daeheon_macbook/Documents/Development/Python - Algo/Nadongbin/honeyboy/CH13-DFS-BFS/q21.txt', 'r')

while True:
    try:

        graph = []

        n, l, r = map(int, input().split())
        for _ in range(n):
            graph.append(list(map(int, input().split())))

        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        def bfs(a, b):
            # dfs (스택)을 이용해 각 요소를 확장, 방문한 요소를 표시
            # 시작 지점 요소를 방문 체크
            q = deque()
            temp = []
            q.append((a, b))
            temp.append((a, b))
            while q:
                x, y = q.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if (0 <= nx < n and 0 <= ny < n and flagBaseGrid[nx][ny] == False):
                        if (l <= abs(
                                graph[x][y] - graph[nx][ny]) <= r):
                            flagBaseGrid[nx][ny] = True
                            q.append((nx, ny))
                            temp.append((nx, ny))

            return temp

        loopCnt = 0

        # 모든 그리드의 요소를 순환
        while 1:
            flagBaseGrid = [[False] * (n + 1)
                            for _ in range(n + 1)]
            jobNeeded = False
            for i in range(n):
                for j in range(n):
                    if (flagBaseGrid[i][j] == False):
                        flagBaseGrid[i][j] = True
                        adjList = bfs(i, j)
                        if (len(adjList) > 1):
                            jobNeeded = True
                            res = sum([graph[x][y]
                                       for x, y in adjList]) // len(adjList)
                            for x, y in adjList:
                                graph[x][y] = res
            if jobNeeded == False:
                break
            loopCnt += 1

        print(loopCnt)

    except EOFError:
        print("process finished")
        break
