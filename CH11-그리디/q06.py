# 다음의 링크에서 코드를 실행합니다 https://school.programmers.co.kr/learn/courses/30/lessons/42891

# 첫번째 시도

"""
def eat(x):
    if(x >= 1):
        return x - 1
    else:
        return x

def solution(food_times, k):
    
    if sum(food_times) <= k:
        return -1
    
    i = 0
    countdown = k
    foodLength = len(food_times)
    
    while True:
        remainCount = len(food_times) - food_times.count(0)
        if(countdown > remainCount):
            countdown -= remainCount
            food_times = list(map(eat, food_times))
        else:
            while(countdown > 0):
                if(food_times[i] != 0):
                    countdown -= 1
                i += 1
            break
    
    if((i+1)>foodLength):
        answer = 1
    else:
        answer = i+1
        
    return answer
"""

# 책 코드 카피

import heapq


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))

    sum_value = 0
    previous = 0
    length = len(food_times)

    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1
        previous = now

    result = sorted(q, key=lambda x: x[1])
    return result[(k - sum_value) % length][1]

# 3번째 시도


def solution(food_times, k):

    if sum(food_times) <= k:
        return -1

    q = []
    foodCount = len(food_times)

    for i in range(foodCount):
        heapq.heappush(q, (food_times[i], i + 1))

    timeRemain = k
    foodRemainCount = foodCount
    timeExpected = 0
    previousTimeExpected = 0
    timeUsed = 0

    while ((q[0][0] - previousTimeExpected) * foodRemainCount + timeUsed <= timeRemain):
        timeExpected = heapq.heappop(q)[0]
        timeUsed += (timeExpected - previousTimeExpected) * foodRemainCount
        foodRemainCount -= 1
        previousTimeExpected = timeExpected

    result = sorted(q, key=lambda x: x[1])
    return result[(timeRemain - timeUsed) % foodRemainCount][1]
