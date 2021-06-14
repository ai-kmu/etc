class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        stack = []
        answer = 0
        # 각 노드의 visited를 False로 설정한다.
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        for m in range(len(grid)):
            for n in range(len(grid[0])):
                # 만약 이전에 방문했을 경우 건너뛴다.
                if visited[m][n]:
                    continue
                visited[m][n] = True
                # 만약 현재 위치가 땅일 경우 새로운 섬을 발견한 것으로 여겨 stack에 추가한다.
                if grid[m][n] == '1':
                    stack.append((m,n))
                    answer += 1
                # DFS를 활용해 섬에 포함되는 땅을 모두 찾아낸 후 visited를 True로 설정한다.
                while stack:
                    row, col = stack.pop()
                    # 모서리에 있는 경우를 제외하고 상하좌우 방향을 설정한다.
                    directions = [(-1, 0) if row != 0 else False, 
                                  (1, 0) if row != len(grid)-1 else False,
                                  (0, -1) if col != 0 else False, 
                                  (0, 1) if col != len(grid[0])-1 else False]
                    for d in directions:
                        if d:
                            # 상하좌우 위치의 노드가 1이고 아직 방문하지 않은 경우 stack에 추가한다.
                            nextRow = row + d[0]
                            nextCol = col + d[1]
                            if grid[nextRow][nextCol] == '1' and not visited[nextRow][nextCol]:
                                stack.append((nextRow, nextCol))
                                visited[nextRow][nextCol] = True
        return answer
