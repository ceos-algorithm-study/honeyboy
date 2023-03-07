from re import L
import sys
from collections import deque

sys.stdin = open(
    '/Users/daeheon_macbook/Documents/Development/Python - Algo/Nadongbin/honeyboy/CH6-정렬/q02.txt', 'r')


while True:
    try:
        n = int(input())
        array = []
        for i in range(n):
            array.append(input())

        for j in range(n):
            for k in range(j, n):
                if (array[j] < array[k]):
                    array[j], array[k] = array[k], array[j]

        for m in range(n):
            print(array[m])

    except EOFError:
        print("process finished")
        break
