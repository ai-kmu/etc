def solution(p, l):
    q = [(i, p) for (i, p) in enumerate(p)]
    a = 0

    while q != None:
        f = q.pop(0)

        # https://docs.python.org/3/library/functions.html#any
        if any(f[1] < p[1] for p in q):
            q.append(f)
        else:
            a += 1
            if f[0] == l:
                break

    return a
