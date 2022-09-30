import sys

sys.stdin = open(
    '/Users/daeheon_macbook/Documents/Development/Python - Algo/Nadongbin/honeyboy/CH11-그리디/q01.txt', 'r')

count = int(input())

travlerList = []
travlerList = list(map(int, input().split(' ')))

travlerList.sort()

result = 0
fearLevel = 0
groupCount = 0

for i in range(0, count):
    fearLevel = travlerList[i]
    groupCount = groupCount + 1
    if (fearLevel <= groupCount):
        result += 1
        groupCount = 0

print(result)
