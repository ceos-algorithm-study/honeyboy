import sys
import heapq

sys.stdin = open(
    '/Users/daeheon_macbook/Documents/Development/Python - Algo/Nadongbin/honeyboy/CH12-구현/q08.txt', 'r')

while True:
    try:
        inputString = list(input())
        strings = []
        numberSum = 0
        result = []
        for i in range(0, len(inputString)):
            instance = ord(inputString[i])
            if (instance > 47 and instance < 58):
                numberSum += int(inputString[i])
            else:
                heapq.heappush(strings, (instance, inputString[i]))
        for i in range(0, len(strings)):
            print(heapq.heappop(strings)[1], end="")
        print(numberSum)
    except EOFError:
        print("process finished")
        break
