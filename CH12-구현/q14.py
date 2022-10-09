# 다음의 링크에서 풀이합니다. https://school.programmers.co.kr/learn/courses/30/lessons/60062

from itertools import permutations


def solution(n, weak, dist):
    weak_len = len(weak)
    weak_loop = [*weak]
    weak_loop.extend(list(x + n for x in weak))
    friends_set = list(permutations(dist))
    friends_size = len(dist)
    candidates = []

    for point_idx in range(0, len(weak)):
        for friends in friends_set:
            friend_cnt = 1
            loc = weak_loop[point_idx] + friends[friend_cnt - 1]
            for loop_idx in range(point_idx, point_idx + weak_len):
                if (loc < weak_loop[loop_idx]):
                    friend_cnt += 1
                    if (friend_cnt > friends_size):
                        break
                    loc = weak_loop[loop_idx] + friends[friend_cnt - 1]
            candidates.append(friend_cnt)
    ans = min(candidates)
    if (ans > friends_size):
        ans = -1
    return ans
