from collections import deque, namedtuple
from copy import deepcopy
def solution(maps):
    N = len(maps) - 1
    M = len(maps[0]) - 1

    Position = namedtuple("Position", ["y", "x"])
    Position.__add__ = lambda left, right: Position(left.y + right.y, left.x + right.x)
    State = namedtuple("State", ["map", "pos", "count"])
    
    raw_actions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    actions = list(map(lambda x: Position(*x), raw_actions))
    states = deque([State(maps, Position(0, 0), 1)])
    
    while True:
        if len(states) == 0:
            return -1
        (map_, pos, count) = states.popleft()
        if pos == Position(N, M):
            return count
        for action in actions:
            next_pos = pos + action
            if not 0 <= next_pos.y <= N or not 0 <= next_pos.x <= M:
                continue
            if map_[next_pos.y][next_pos.x] == 1:
                map_[pos.y][pos.x] = -1
                states.append(State(deepcopy(map_), next_pos, count+1))
