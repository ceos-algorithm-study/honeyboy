from re import L
import sys

sys.stdin = open(
    '/Users/daeheon_macbook/Documents/Development/Python - Algo/Nadongbin/honeyboy/CH15-이진 탐색 문제/q28.txt', 'r')

while True:
    try:
        cnt = int(input())
        numberList = list(map(int, input().split(' ')))
        start = 0
        found = False
        end = cnt - 1
        if (cnt == 1):
            if (numberList[0] == 0):
                print("0")
            else:
                print("-1")

        while (start <= end):
            anchor = (end + start) // 2
            if (numberList[anchor] == anchor):
                print(anchor)
                found = True
                break
            elif (numberList[anchor] > anchor):
                end = anchor - 1
            else:
                start = anchor + 1
        if (not found):
            print("-1")

    except EOFError:
        print("process finished")
        break
