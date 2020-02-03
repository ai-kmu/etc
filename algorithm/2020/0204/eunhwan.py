# N 은 색종이의 갯수.
n = int(input())

# 1 ≤ __constant__ ≤ 101
__constant__ = 101

shape, marker = [[0 for i in range(__constant__)] for j in range(__constant__)], 1
markers = dict()

# 로컬에서 확인할 때는 이렇게.
assert len(shape) == __constant__
assert len(shape[0]) == __constant__

for i in range(n):
    x, y, w, h = map(int, input().split())
    markers[marker] = 0

    """
    starting point: x, y
    w: width
    h: height
    """
    for X in range(x, x + w):
        for Y in range(y, y + h):
            shape[X][Y] = marker
    marker += 1


for i in markers:
    for j in range(__constant__):
        markers[i] += sum(list(map(lambda x: x == i, shape[j])))
    print(markers[i])
