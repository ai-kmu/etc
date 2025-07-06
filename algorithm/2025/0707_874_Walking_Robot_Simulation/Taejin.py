# 50번째에서 틀리는데 안풀립니다..

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        x, y = 0, 0
        cur_dir = 0
        max_dist = 0
        sum_dist = 0
        
        # 행, 열 별로 장애물 쉽게 파악하기 위해 dict로 추가
        obstacle_row = defaultdict(set)
        obstacle_col = defaultdict(set)

        for ox, oy in obstacles:
            obstacle_row[ox].add(oy)
            obstacle_col[oy].add(ox)

        commands.append(-1) # 아래 c < 0 도는 마지막 케이스를 위해 dummy -1 추가

        for c in commands:
            print("pos :", x, y)
            if c < 0:
                dx, dy = directions[cur_dir]
                new_x, new_y = x + sum_dist * dx, y + sum_dist * dy

                if dx == 0: # x 이동에 대한 위치 설정
                    for obs_y in obstacle_row[x]:
                        if y * dy < obs_y * dy < new_y * dy:
                            new_y = (min(new_y * dy, obs_y * dy) - 1) * dy

                if dy == 0: # x 이동에 대한 위치 설정
                    for obs_x in obstacle_col[y]:
                        if x * dx < obs_x * dx < new_x * dx:
                            new_x = (min(new_x * dx, obs_x * dx) - 1) * dx
                
                sum_dist = 0
                
                if c == -1:
                    cur_dir = (cur_dir + 1) % 4
                else:
                    cur_dir = (cur_dir - 1) % 4

                max_dist = max(max_dist, new_x**2 + new_y**2)
                x, y = new_x, new_y

            else:
                sum_dist += c

        return max_dist
