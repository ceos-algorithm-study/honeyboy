from re import L
import sys
from collections import deque

sys.stdin = open(
    '/Users/daeheon_macbook/Documents/Development/Python - Algo/Nadongbin/honeyboy/CH7-이진탐색/q02.txt', 'r')


def binary_search(arr, start, end, value):
    if (start > end):
        return None
    mid = (start + end) // 2
    if (arr[mid] == value):
        return mid
    elif (arr[mid] < value):
        return binary_search(arr, mid + 1, end, value)
    elif (arr[mid] > value):
        return binary_search(arr, start, mid - 1, value)


while True:
    try:
        shelfSize = int(input())
        shelf = list(map(int, input().split()))
        orderSize = int(input())
        order = list(map(int, input().split()))
        res = []
        for item in order:
            if (binary_search(shelf, 0, shelfSize - 1, item)):
                res.append("yes")
            else:
                res.append("no")
            # if (item in shelf):
            #     res.append("yes")
            # else:
            #     res.append("no")
        print(res)

    except EOFError:
        print("process finished")
        break
