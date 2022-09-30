import sys

sys.stdin = open(
    '/Users/daeheon_macbook/Documents/Development/Python - Algo/Nadongbin/honeyboy/CH11-그리디/q04.txt', 'r')

count = int(input())
value = list(map(int, input()))
value.sort()

target = 1

for x in count:
    if x > target:
        break
    target += x

print(target)
