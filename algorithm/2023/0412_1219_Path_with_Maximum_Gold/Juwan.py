class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        """
        grid에 0이 하나도 없을 때 바로 전체 합을 리턴하는 부분
        """
        a = set()
        s = 0
        for i in grid:
            s += sum(i)
            for j in i:
                a.add(j)
        if not 0 in a:
            return s
          
        """
        만약 그게 아닌 경우  DFS로 풀이
        """
        
        m = len(grid)
        n = len(grid[0])

        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        max_reward = 0

        def backtrack(g, x, y, reward):

            if g[x][y] == 0:
                return reward

            reward += g[x][y]
            g[x][y] = 0
            max_r = 0
            
            for i, j in zip(dx, dy):
                if 0 <= x - i < m and 0 <= y - j < n:
                    temp = [item[:] for item in g] # deepcopy와 동일한 연산. 그러나 100배 빠름
                    max_r = max(max_r, backtrack(temp, x - i, y - j, reward))

            return max_r

        for i in range(m):
            for j in range(n):
                bt = [item[:] for item in grid] # deepcopy와 동일한 연산. 그러나 100배 빠름
                max_reward = max(max_reward, backtrack(bt, i, j, 0))
        
        return max_reward
