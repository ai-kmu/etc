from collections import deque, namedtuple
from copy import deepcopy
def solution(maps):
    N = len(maps) - 1
    M = len(maps[0]) - 1

    Position = namedtuple("Position", ["y", "x"])
    Position.__add__ = lambda left, right: Position(left.y + right.y, left.x + right.x)
    Position.is_out_of_range = lambda self: not 0 <= self.y <= N or not 0 <= self.x <= M
    State = namedtuple("State", ["map", "pos", "depth"])
    
    raw_actions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    actions = list(map(lambda x: Position(*x), raw_actions))
    states = deque([State(maps, Position(0, 0), 1)])
    
    while True:
        if len(states) == 0: return -1
        (map_, pos, depth) = states.popleft()
        if pos == Position(N, M): return depth
        for action in actions:
            next_pos = pos + action
            if next_pos.is_out_of_range(): continue
            if map_[next_pos.y][next_pos.x] == 1:
                map_[pos.y][pos.x] = -1
                states.append(State(deepcopy(map_), next_pos, depth+1))
