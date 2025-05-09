from collections import defaultdict, deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # bfs
        visited = defaultdict(int)
        cur_points = deque()
        cnt = 0
        cur_points.append([0,0,0,0])

        get_str_point = lambda x: "".join(map(str, x))
        
        for dead in deadends:
            visited[dead] = -1

        if visited['0000'] == -1:
            return -1

        while cur_points:
            cur_point = cur_points.popleft()
            cur_str_point = get_str_point(cur_point)
            # print("depth :", visited[cur_str_point])
            # print(cur_str_point)
            
            if cur_str_point == target:
                return visited[cur_str_point]
            
            for i in range(4):
                for move in [-1, 1]:
                    new_point = cur_point[:]
                    new_point[i] = (new_point[i] + move) % 10
                    new_str_point = get_str_point(new_point)
                    if visited[new_str_point] == 0:
                        visited[new_str_point] = visited[cur_str_point] + 1
                        cur_points.append(new_point)

        return -1
