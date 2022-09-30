import sys

sys.stdin = open(
    '/Users/daeheon_macbook/Documents/Development/Python - Algo/Nadongbin/honeyboy/CH11-그리디/q03.txt', 'r')

value = list(map(int, input()))
count = len(value)
startIndex = 0
lastIndex = count - 1
anchor = value[startIndex]


def reverse(value, s, e):
    for i in range(s, e + 1):
        value[i] = str(1 - int(value[i]))


while (startIndex < lastIndex-1):
    if (value[startIndex] == anchor):
        startIndex += 1
    if (value[lastIndex] == anchor):
        lastIndex -= 1
    if (value[lastIndex] != anchor and value[startIndex] != anchor):
        reverse(value, startIndex, lastIndex)
