# https://programmers.co.kr/learn/courses/30/lessons/60060

from bisect import bisect_left, bisect_right


def countWords(wordList, start, end):
    left = bisect_left(wordList, start)
    right = bisect_right(wordList, end)
    return (right - left)


def solution(words, queries):
    normal_words_by_length = [[] for i in range(10001)]
    reverse_words_by_length = [[] for j in range(10001)]
    res = []

    for word in words:
        normal_words_by_length[len(word)].append(word)
        reverse_words_by_length[len(word)].append(word[::-1])

    for k in range(10001):
        normal_words_by_length[k].sort()
        reverse_words_by_length[k].sort()

    for query in queries:
        if (query[0] != '?'):
            temp = countWords(normal_words_by_length[len(query)], query.replace(
                '?', 'a'), query.replace('?', 'z'))
            res.append(temp)
        else:
            temp = countWords(reverse_words_by_length[len(
                query)], query[::-1].replace('?', 'a'), query[::-1].replace('?', 'z'))
            res.append(temp)

    return res
