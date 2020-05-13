from collections import deque, namedtuple
def solution(maps):
    N, M = len(maps) - 1, len(maps[0]) - 1
    Pos = namedtuple("Position", ["y", "x"])
    Pos.__add__ = lambda lhs, rhs: Pos(lhs.y + rhs.y, lhs.x + rhs.x)
    Pos.is_out_of_range = lambda self: not 0 <= self.y <= N or not 0 <= self.x <= M
    
    raw_directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    directions = list(map(lambda x: Pos(*x), raw_directions))
    q = deque([(Pos(0, 0), 1)])
    
    while True:
        if len(q) == 0: return -1
        pos, depth = q.popleft()
        if pos == Pos(N, M): return depth
        for d in directions:
            next_pos = pos + d
            if next_pos.is_out_of_range(): continue
            if maps[next_pos.y][next_pos.x] == 1:
                maps[pos.y][pos.x] = -1
                q.append((next_pos, depth+1))
