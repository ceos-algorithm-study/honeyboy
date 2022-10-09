# 다음의 링크에서 풀이한다 https://school.programmers.co.kr/learn/courses/30/lessons/60057

import math


def divide_into_chunks(li, n):
    for i in range(0, len(li), n):
        yield li[i:i + n]


def solution(s):

    interval = 1
    strings = list(s)
    length = len(strings)
    limit = length // 2
    minLengthList = []

    if (limit < 1):
        return 1

    while (interval <= limit):
        dividedStrings = list(divide_into_chunks(strings, interval))
        totalLen = 0
        chainLen = 1
        isChain = False

        for i in range(0, len(dividedStrings)-1):
            if (dividedStrings[i] == dividedStrings[i+1]):
                isChain = True
                chainLen += 1
            elif ((dividedStrings[i] != dividedStrings[i+1]) and isChain):
                isChain = False
                totalLen += (interval + int(math.log10(chainLen)) + 1)
                chainLen = 1
            else:
                totalLen += interval

        if (isChain):
            totalLen += (interval + int(math.log10(chainLen)) + 1)
        else:
            totalLen += len(dividedStrings[i+1])

        minLengthList.append(totalLen)
        interval += 1

    return min(minLengthList)
