def solution(tri):
    current = tri[-1]
    for t in tri[-2::-1]:
        x = [sum(x) for x in zip(t, current)]
        y = [sum(x) for x in zip(t, current[1:])]
        current = [max(*n) for n in zip(x, y)]
    return current[0]
