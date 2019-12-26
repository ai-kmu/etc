from collections import deque


def solution(begin, target, words):
    levelize = lambda s, t: sum((1 if x is not y else 0) for x, y in zip(s, t)) is 1
    q, d = deque(), dict()
    q.append((begin, 0))
    d[begin] = set(filter(lambda x: levelize(x, begin), words))

    for w in words:
        d[w] = set(filter(lambda x: levelize(x, w), words))

    while q:
        c, l = q.popleft()
        for w in d[c]:
            if w is target:
                return l + 1
            else:
                q.append((w, l + 1))
    else:
        return 0


begin, target = 'hit', 'cog'
words = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']
# levelize = lambda a, b: sum((1 if x != y else 0) for x, y in zip(a, b)) == 1
# for w in words:
#     print(set(filter(lambda x: levelize(x, w), words)))
#
print(solution(begin, target, words))
