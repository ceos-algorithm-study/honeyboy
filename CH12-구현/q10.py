# 다음의 링크에서 풀이한다 https://school.programmers.co.kr/learn/courses/30/lessons/60059

from copy import deepcopy
from itertools import chain

def checkAnswer (key, lock):
    lockLength = len(lock)
    keyLength = len(key)
    
    for x in range(1 - lockLength, lockLength):
        for y in range(1 - lockLength, lockLength):
            res = deepcopy(lock)
            for i in range(0, keyLength):
                for j in range(0, keyLength):
                    if((x+i >= 0 and y+j >= 0) and (x+i < lockLength and y+j < lockLength)):
                        res[y+j][x+i] += key[j][i]
            
            isOpen = all(elem == 1 for elem in chain(*res))
            if(isOpen): return True         
    return False

def rotateMatrixCW (mat):
    return list(zip(*mat[::-1]))

def solution(key, lock):

    for i in range(0, 4):
        isOpen = checkAnswer(key, lock)
        if(isOpen): return True
        key = rotateMatrixCW(key)
        
    return False