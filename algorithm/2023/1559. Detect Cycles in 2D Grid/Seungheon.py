class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:

        # dfs
        def explore(i, j, ch, count = 0):
            nonlocal visited, answer

            # 답을 구했으면 더이상 탐색하지 않음
            if answer:
                return

            # 범위 밖이면 안감
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return
            
            # 다른모양이면 안감
            if grid[i][j] != ch:
                return
            
            # 방문 했고, 차이가 2 이하면 안감
            if visited[i][j] != 0 and count - visited[i][j] <= 2:
                return

            # 방문했고, 차이가 2 이상이면 정답
            if visited[i][j] != 0 and count - visited[i][j] > 2:
                answer = True
                return

            # 방문처리
            count += 1
            visited[i][j] = count

            for dy, dx in [[1,0],[0,1],[-1,0],[0,-1]]:
                explore(i+dy,j+dx, ch, count)
                if answer:
                    return

        answer = False        
        visited = [[ 0 for _ in range(len(grid[0]))]for _ in range(len(grid))]

        # 모든 셀에서 시작
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                explore(i, j, grid[i][j], 0)
                if answer:
                    return True

        return False
