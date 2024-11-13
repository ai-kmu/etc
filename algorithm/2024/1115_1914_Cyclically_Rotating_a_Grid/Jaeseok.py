from collections import deque

class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        x, y, cycle = 0, 0, 0
        x_min, y_min, x_max, y_max = 0, 0, m - 1, n - 1
        new_grid = [[0] * n for _ in range(m)]
        # 전체 사이클 수는 짧은 쪽의 절반
        while cycle < min(m, n) // 2:
            # grid rotation은 각 해당 줄의 rotation으로 문제를 쪼갤 수 있음
            # deque를 통해 rotation 구현
            arrange_list = deque()
            # 해당 줄을 순회하면서 arrange_list에 저장
            while y < y_max:
                arrange_list.append(grid[x][y])
                y += 1
            while x < x_max:
                arrange_list.append(grid[x][y])
                x += 1
            while y > y_min:
                arrange_list.append(grid[x][y])
                y -= 1
            while x > x_min:
                arrange_list.append(grid[x][y])
                x -= 1

            # 현재 줄의 길이만큼 돌면 똑같아지므로 돌되 k로 나누어 불필요한 rotation 방지
            for _ in range(k % len(arrange_list)):
                arrange_list.append(arrange_list.popleft())

            # rotation 후에 다시 재할당
            while y < y_max:
                new_grid[x][y] = arrange_list.popleft()
                y += 1
            while x < x_max:
                new_grid[x][y] = arrange_list.popleft()
                x += 1
            while y > y_min:
                new_grid[x][y] = arrange_list.popleft()
                y -= 1
            while x > x_min:
                new_grid[x][y] = arrange_list.popleft()
                x -= 1
            
            # 다음 사이클을 위해 최대, 최솟값, 시작 커서 재지정
            x_min += 1
            y_min += 1
            x_max -= 1
            y_max -= 1
            x += 1
            y += 1

            cycle += 1
        
        return new_grid
        
