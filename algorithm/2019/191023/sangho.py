def solution(tri):
    current_line = tri[-1]
    for t in tri[-2::-1]:
        x = [sum(x) for x in zip(t, current_line)]
        y = [sum(x) for x in zip(t, current_line[1:])]
        current_line = [max(*n) for n in zip(x, y)]
    return current_line[0]