import sys

sys.stdin = open(
    '/Users/daeheon_macbook/Documents/Development/Python - Algo/Nadongbin/honeyboy/CH11-그리디/q05.txt', 'r')

while True:
    try:
        count, maxWeight = map(int, (input().split()))
        value = list(map(int, input().split()))
        instance = 0
        duplicate = 0

        for i in range(1, maxWeight + 1):
            duplicate = value.count(i)
            if (duplicate > 1):
                duplicate = duplicate * (duplicate - 1)
                instance += duplicate
            duplicate = 0

        result = count * (count - 1)
        result = int((result - instance)/2)
        print(result)

    except EOFError:
        print("process finished")
        break
