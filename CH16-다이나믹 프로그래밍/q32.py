from re import L
import sys

sys.stdin = open(
    '/Users/daeheon_macbook/Documents/Development/Python - Algo/Nadongbin/honeyboy/CH16-다이나믹 프로그래밍/q32.txt', 'r')

while True:
    try:
        depth = int(input())
        prevMaxArray = [0 for _ in range(depth + 1)]
        inputArray = [[] for _ in range(depth)]
        for i in range(depth):
            inputArray[i] = list(map(int, input().split()))

        for depthIdx in range(depth - 1, 0, -1):
            for rowIdx in range(depthIdx + 1):
                prevMaxArray[rowIdx] = max(
                    inputArray[depthIdx][rowIdx] + prevMaxArray[rowIdx], inputArray[depthIdx][rowIdx] + prevMaxArray[rowIdx + 1])

        print(str(max(inputArray[0][0] + prevMaxArray[0],
              inputArray[0][0] + prevMaxArray[1])))

    except EOFError:
        print("process finished")
        break
