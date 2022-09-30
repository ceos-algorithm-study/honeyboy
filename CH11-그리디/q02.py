import sys

sys.stdin = open(
    '/Users/daeheon_macbook/Documents/Development/Python - Algo/Nadongbin/honeyboy/CH11-그리디/q02.txt', 'r')

numbers = list(map(int, input()))
print(numbers)

result = 0

for i in range(1, len(numbers)):
    if (numbers[i-1] == 0):
        result += numbers[i]
    else:
        result *= numbers[i]

print(result)
