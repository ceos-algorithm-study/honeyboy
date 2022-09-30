import sys

sys.stdin = open(
    '/Users/daeheon_macbook/Documents/Development/Python - Algo/Nadongbin/honeyboy/CH12-구현/q07.txt', 'r')

while True:
    try:
        numbers = list(map(int, list(input())))
        length = len(numbers)
        idx = length // 2
        if (sum(numbers[:idx]) == sum(numbers[idx:])):
            print("LUCKY")
        else:
            print("READY")

    except EOFError:
        print("process finished")
        break
