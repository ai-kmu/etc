# 시간 초과
# first_search에서 최대 체리를 집지 않은 경우에도 최종적으로 최대 체리를 집는 경우가 있다.
# 구현해보려 했으나 실패
# 이 코드는 first_search의 모든 경우를 따지기에 시간 초과난다.

from collections import deque
from copy import deepcopy

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        idx_len = len(grid)-1
        start_cherry = grid[0][0]

        flag = 0
        # trivial case
        if idx_len == 0:
            return start_cherry

        first_move = [(0,1), (1,0)]
        second_move = [(0,-1), (-1,0)]    

        first_sp = (0,0)
        second_sp = (idx_len, idx_len)

        first_complete = []
        second_complete = []

        # first search
        q = deque()

        # start x, y, route, cherry 개수 지정
        q.append((first_sp[0], first_sp[0], [first_sp], start_cherry))

        while q:
            a = q.popleft()
            x, y, route, pre_cnt = a[0], a[1], a[2], a[3]

            # check cherry
            if x == y == 0:
                now_cnt = pre_cnt
            else:
                now_cnt = pre_cnt + 1 if grid[x][y] == 1 else pre_cnt

            # check end-point
            if x == y == idx_len:

                first_complete.append((a[2],now_cnt))


            for dx,dy in first_move:
                now_x, now_y = x+dx, y+dy

                # check idx
                if now_x > idx_len or now_y > idx_len:
                    continue
                if grid[now_x][now_y] == -1:
                    continue
                r = copy.deepcopy(route)
                r.append((now_x,now_y))
                q.append((now_x, now_y, r, now_cnt))
        if len(first_complete) == 0:
            return 0

        # second search        
        for r in first_complete:
            route = r[0]
            second_start_cherry = r[1]
            # 각 case route 반영한 grid 생성
            tmp_grid = copy.deepcopy(grid)
            for i, j in r[0]:
                tmp_grid[i][j] = 0

            # start x, y, route, cherry 개수 지정
            q.append((second_sp[0], second_sp[1], [second_sp], second_start_cherry))
            while q:
                a = q.popleft()
                x, y, route, pre_cnt = a[0], a[1], a[2], a[3]

                # check cherry
                if x == y == idx_len:
                    now_cnt = pre_cnt
                else:
                    now_cnt = pre_cnt + 1 if tmp_grid[x][y] == 1 else pre_cnt

                # check end-point
                if x == y == 0:
                    second_complete.append(now_cnt)

                for dx,dy in second_move:
                    now_x, now_y = x+dx, y+dy

                    # check idx
                    if now_x < 0 or now_y < 0:
                        continue
                    if tmp_grid[now_x][now_y] == -1:
                        continue
                    r = copy.deepcopy(route)
                    r.append((now_x,now_y))
                    q.append((now_x, now_y, r, now_cnt))

        return max(second_complete)
