from re import L
import sys
from collections import deque

sys.stdin = open(
    '/Users/daeheon_macbook/Documents/Development/Python - Algo/Nadongbin/honeyboy/CH6-정렬/q03.txt', 'r')


while True:
    try:
        n = int(input())
        student = [0 for _ in range(n)]
        for i in range(n):
            student[i] = list(input().split())
            print(student[i])
        res = sorted(student, key=lambda student: student[1])
        for studentBlock in res:
            print(studentBlock[0], end=' ')
    except EOFError:
        print("process finished")
        break
