class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        l = len(grid)
        memo = {}

        def dfs(a1,b1,a2,b2):

            if a1 == l-1 and b1 == l-1 and a2 == l-1 and b2 == l-1:
                return grid[a1][b1]

            # 갈 수 없는 곳이나 가는 곳이 grid index 벗어나면 음수로 큰값을 리턴
            if max(a1,b1,a2,b2) >= l or grid[a1][b1] == -1 or grid[a2][b2] == -1:
                return -10000
            # 두 사람의 좌표 이미 방문한 경우는 저장한 것 리턴
            # memoization을 통해 중복 계산 방지
            if (a1,b1,a2,b2) in memo:
                return memo[(a1,b1,a2,b2)]
            
            # 정답값
            res = 0 
            # 두 사람의 좌표가 같으면 중복해서 res에 더하지 않도록 함
            # 같지 않으면 모두 더함
            if (a1,b1) == (a2,b2):
                res += grid[a1][b1]
            else:
                res += (grid[a1][b1] + grid[a2][b2])

            # 
            res += max(dfs(a1+1,b1,a2,b2+1), dfs(a1,b1+1,a2+1,b2), dfs(a1+1,b1,a2+1,b2), dfs(a1,b1+1,a2,b2+1))
            memo[(a1,b1,a2,b2)] = res

            return res
        res = dfs(0,0,0,0)
        return res if res > 0 else 0
