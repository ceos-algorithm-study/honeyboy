        gridSize, lwBound, upBound = map(int, input().split())
        for _ in range(gridSize):
            grid.append(list(map(int, input().split())))

        dy = [0, 0, 1, -1]
        dx = [1, -1, 0, 0]

        def bfs(y, x):
            # dfs (스택)을 이용해 각 요소를 확장, 방문한 요소를 표시
            # 시작 지점 요소를 방문 체크
            arr = deque()
            valArr = []
            arr.append((y, x))
            valArr.append((y, x))
            while arr:
                y, x = arr.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if (0 <= nx < gridSize and 0 <= ny < gridSize and flagBaseGrid[ny][nx] == False):
                        if (lwBound <= abs(
                                grid[y][x] - grid[ny][nx]) <= upBound):
                            flagBaseGrid[ny][nx] = True
                            arr.append((ny, nx))
                            valArr.append((ny, nx))

            return valArr

        loopCnt = 0

        # 모든 그리드의 요소를 순환
        while (True):
            flagBaseGrid = [[False] * (gridSize + 1)
                            for _ in range(gridSize + 1)]
            jobNeeded = False
            for y in range(gridSize):
                for x in range(gridSize):
                    if (flagBaseGrid[y][x] == False):
                        flagBaseGrid[y][x] = True
                        adjList = bfs(y, x)
                        if (len(adjList) > 1):
                            jobNeeded = True
                            res = sum([grid[y][x]
                                       for y, x in adjList]) // len(adjList)
                            for y, x in adjList:
                                grid[y][x] = res
            if jobNeeded == False:
                break
            loopCnt += 1

        print(loopCnt)