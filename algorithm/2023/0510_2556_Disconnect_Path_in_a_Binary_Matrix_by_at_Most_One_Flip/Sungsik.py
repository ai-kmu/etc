class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        if m == 1 and n <= 2:
            return False
        # 가능한 모든 path들 중에서 서로 겹치지 않는 path 쌍이 존재한다면 이는 False
        # 그렇지 않다면 True
        # 그렇다고 가능한 모든 path들을 구하고 모두 겹치는지 확인하는 것은 시간이 오래 걸림
        # 따라서 오른쪽이 우선인 path와 아래쪽이 우선인 path 2개만 구해서 겹치는지만 확인해도 됨
        grid[0][0] = 0
        dirs = [(0, 1), (1, 0)]
        answer = 0
        
        def dfs(y, x, path):
            if y == m - 1 and x == n - 1:
                return path, True
            for dy, dx in dirs:
                new_y, new_x = y + dy, x + dx
                if new_y < m and new_x < n and grid[new_y][new_x]:
                    grid[new_y][new_x] = 0
                    new_path, result = dfs(new_y, new_x, path)
                    grid[new_y][new_x] = 1
                    if result:
                        new_path.append((new_y, new_x))
                        return new_path, True
                    
            return path, False
        
        first_path, _ = dfs(0, 0, [])
        first_path = set(first_path)
        dirs = dirs[::-1]
        second_path, _ = dfs(0, 0, [])
        second_path = set(second_path)
        
        # 마지막 위치가 무조건 겹치므로 안겹치는지 확인하기 위해 개수를 1과 비교
        return len(first_path & second_path) != 1
