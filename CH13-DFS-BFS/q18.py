# programmers.co.kr/learn/courses/30/lessons/60058

def divideString(stringData):
    leftTildeCnt = 0
    rightTildeCnt = 0
    if not stringData:
        return ""

    # check 균형잡힌 괄호 문자열
    idx = 0
    for i, character in enumerate(stringData):
        if (character == "("):
            leftTildeCnt += 1
        elif (character == ")"):
            rightTildeCnt += 1
        if (leftTildeCnt == rightTildeCnt):
            idx = i
            break
    u = stringData[:idx + 1]
    v = stringData[idx + 1:]

    # check 올바른 괄호 문자열
    stack = []
    flag = True
    for chracter in u:
        if (character == "("):
            stack.append(1)
        if (stack and character == ")"):
            stack.pop()

    # stack이 비지 않은 경우, 올바르지 않음
    if (stack):
        res = ""
        res = "(" + divideString(v) + ")"
        temp = u[1:-1]
        for character in temp:
            if (character == "("):
                res = res + ")"
            elif (character == ")"):
                res = res + "("
        return res
    # 올바른 경우 나머지에 대해 처리
    else:
        res = u + divideString(v)
        return res


def solution(p):
    answer = divideString(p)
    return answer
