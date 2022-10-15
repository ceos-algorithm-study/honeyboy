# https://programmers.co.kr/learn/courses/30/lessons/60063
import sys
from collections import deque

sys.stdin = open(
    '/Users/daeheon_macbook/Documents/Development/Python - Algo/Nadongbin/honeyboy/CH13-DFS-BFS/q22.txt', 'r')

while True:
    try:
        # def getHrCase(paddedBoard, curpos):
        #     res = []
        #     pt1 = curpos[0]
        #     pt2 = curpos[1]
        #     cnt = curpos[2]
        #     if (paddedBoard[pt1[0] + 1][pt1[1]] == 0 and paddedBoard[pt2[0] + 1][pt2[1]] == 0):
        #         # 수평 하강
        #         res.append(
        #             [[pt1[0] + 1, pt1[1]], [pt2[0] + 1, pt2[1]], cnt + 1])
        #         # 좌 하강 90도
        #         res.append(
        #             ((pt1[0], pt1[1]), (pt2[0] + 1, pt2[1] - 1), cnt + 1))
        #         # 우 하강 90도
        #         res.append(((pt1[0] + 1, pt1[1] + 1),
        #                    (pt2[0], pt2[1]), cnt + 1))
        #     if (paddedBoard[pt1[0] - 1][pt1[1]] == 0 and paddedBoard[pt2[0] - 1][pt2[1]] == 0):
        #         # 수평 상승
        #         res.append(
        #             ((pt1[0] - 1, pt1[1]), (pt2[0] - 1, pt2[1]), cnt + 1))
        #         # 좌 상승 90도
        #         res.append(
        #             ((pt1[0], pt1[1]), (pt2[0] - 1, pt2[1] - 1), cnt + 1))
        #         # 우 상승 90도
        #         res.append(((pt1[0] - 1, pt1[1] + 1),
        #                    (pt2[0], pt2[1]), cnt + 1))
        #     if (paddedBoard[pt1[0]][pt1[1] - 1] == 0 and paddedBoard[pt2[0]][pt2[1] - 1] == 0):
        #         # 수평 좌 이동
        #         res.append(
        #             ((pt1[0], pt1[1] - 1), (pt2[0], pt2[1] - 1), cnt + 1))
        #     if (paddedBoard[pt1[0]][pt1[1] + 1] == 0 and paddedBoard[pt2[0]][pt2[1] + 1] == 0):
        #         # 수평 우 이동
        #         res.append(
        #             ((pt1[0], pt1[1] + 1), (pt2[0], pt2[1] + 1), cnt + 1))
        #     return res

        # def getVlCase(paddedBoard, curpos):
        #     res = []
        #     pt1 = curpos[0]
        #     pt2 = curpos[1]
        #     cnt = curpos[2]
        #     if (paddedBoard[pt1[0] + 1][pt1[1]] == 0 and paddedBoard[pt2[0] + 1][pt2[1]] == 0):
        #         # 수직 하강
        #         res.append(
        #             ((pt1[0] + 1, pt1[1]), (pt2[0] + 1, pt2[1]), cnt + 1))
        #     if (paddedBoard[pt1[0] - 1][pt1[1]] == 0 and paddedBoard[pt2[0] - 1][pt2[1]] == 0):
        #         # 수직 상승
        #         res.append(
        #             ((pt1[0] - 1, pt1[1]), (pt2[0] - 1, pt2[1]), cnt + 1))
        #     if (paddedBoard[pt1[0]][pt1[1] - 1] == 0 and paddedBoard[pt2[0]][pt2[1] - 1] == 0):
        #         # 수직 좌 이동
        #         res.append(
        #             ((pt1[0], pt1[1] - 1), (pt2[0], pt2[1] - 1), cnt + 1))
        #         # 좌 상승 90도
        #         res.append(
        #             ((pt1[0], pt1[1]), (pt2[0] - 1, pt2[1] - 1), cnt + 1))
        #         # 좌 하강 90도
        #         res.append(((pt1[0] + 1, pt1[1] - 1),
        #                    (pt2[0], pt2[1]), cnt + 1))
        #     if (paddedBoard[pt1[0]][pt1[1] + 1] == 0 and paddedBoard[pt2[0]][pt2[1] + 1] == 0):
        #         # 수직 우 이동
        #         res.append(
        #             ((pt1[0], pt1[1] + 1), (pt2[0], pt2[1] + 1), cnt + 1))
        #         # 우 상승 90도
        #         res.append(
        #             ((pt1[0], pt1[1]), (pt2[0] - 1, pt2[1] + 1), cnt + 1))
        #         # 우 하강 90도
        #         res.append(((pt1[0] + 1, pt1[1] + 1),
        #                    (pt2[0], pt2[1]), cnt + 1))
        #     return res

        def can_move(cur1, cur2, new_board):
            Y, X = 0, 1
            cand = []
            # 평행이동
            DELTAS = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            for dy, dx in DELTAS:
                nxt1 = (cur1[Y] + dy, cur1[X] + dx)
                nxt2 = (cur2[Y] + dy, cur2[X] + dx)
                if new_board[nxt1[Y]][nxt1[X]] == 0 and new_board[nxt2[Y]][nxt2[X]] == 0:
                    cand.append((nxt1, nxt2))
            # 회전
            if cur1[Y] == cur2[Y]:  # 가로방향 일 때
                UP, DOWN = -1, 1
                for d in [UP, DOWN]:
                    if new_board[cur1[Y]+d][cur1[X]] == 0 and new_board[cur2[Y]+d][cur2[X]] == 0:
                        cand.append((cur1, (cur1[Y]+d, cur1[X])))
                        cand.append((cur2, (cur2[Y]+d, cur2[X])))
            else:  # 세로 방향 일 때
                LEFT, RIGHT = -1, 1
                for d in [LEFT, RIGHT]:
                    if new_board[cur1[Y]][cur1[X]+d] == 0 and new_board[cur2[Y]][cur2[X]+d] == 0:
                        cand.append(((cur1[Y], cur1[X]+d), cur1))
                        cand.append(((cur2[Y], cur2[X]+d), cur2))

            return cand

        def solution(board):
            size = len(board)
            # 테두리를 1로 채우기
            paddedBoard = [[1]*(size + 2) for _ in range(size + 2)]
            for j in range(1, size + 1):
                for i in range(1, size + 1):
                    paddedBoard[j][i] = board[j - 1][i - 1]
            robotPoses = deque([((1, 1), (1, 2), 0)])
            confirm = set([((1, 1), (1, 2))])
            while robotPoses:
                curpos = robotPoses.popleft()
                if (curpos[0] == (size, size) or curpos[1] == (size, size)):
                    return curpos[2]
                for item in can_move(curpos[0], curpos[1], paddedBoard):
                    if item not in confirm:
                        robotPoses.append((*item, curpos[2] + 1))
                        confirm.add(item)
                # # y축 값이 같다면 - 수평 상태
                # elif ((curpos[0][0] - curpos[1][0]) == 0):
                #     res = getHrCase(paddedBoard, curpos)
                #     robotPoses.extend(res)
                # # x축 값이 같다면 - 수직 상태
                # elif ((curpos[0][1] - curpos[1][1]) == 0):
                #     res = getVlCase(paddedBoard, curpos)
                #     robotPoses.extend(res)
        res = solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [
                       0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]])
        print(res)
        print("process finished")
        break
    except EOFError:
        print("process finished")
        break
