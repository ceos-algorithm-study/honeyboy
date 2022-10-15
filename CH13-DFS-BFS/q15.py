from re import L
import sys
from collections import deque

sys.stdin = open(
    '/Users/daeheon_macbook/Documents/Development/Python - Algo/Nadongbin/honeyboy/CH13-DFS-BFS/q1.txt', 'r')


while True:
    try:
        [cityCnt, roadCnt, opLen, startCity] = list(map(int, input().split()))
        dests = [[] for _ in range(cityCnt + 1)]
        for i in range(roadCnt):
            [st, dt] = list(map(int, input().split()))
            dests[st].append(dt)
        dists = [-1] * (cityCnt + 1)
        dists[startCity] = 0

        q = deque([startCity])
        while q:
            now = q.popleft()
            for next_node in dests(now):
                if (dists[next_node] == -1):
                    dists[next_node] = dists[now] + 1
                    q.append(next_node)

        check = False
        for i in range(1, cityCnt+1):
            if dists[i] == opLen:
                print(i)
                check = True

        if (check == False):
            print(-1)

        print("process finished")
        break
    except EOFError:
        print("process finished")
        break
