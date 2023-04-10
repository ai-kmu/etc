class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        greatest = 0
        
        starts = []
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] != 0:
                    q = collections.deque([])
                    # 금이 들어있는 위치 저장
                    q.append((row, col, [(row, col)], grid[row][col]))
                    maxx = 0
                    # 위치를 찾은 상태이면
                    while q:
                        # row, column, 인덱스, 금 개수를 다음 변수에 저장
                        r, c, path, total = q.popleft()
                        # 처음: 0과 6사이에 비교, 최대값 갱신과정
                        maxx = max(maxx, total)
                        # 모든 방향 이동하며 확인(BFS)
                        for y, x in directions:
                            nr = r + y
                            nc = c + x
                            # 이동했을때 범위를 벗어나지 않으면 + 0이 아니고, 제자리가 아닌경우
                            if nr >= 0 and nr < rows and nc >= 0 and nc < cols and \
                               grid[nr][nc] != 0 and (nr, nc) not in path:
                               # q에 다음위치를 저장하지만, 단 maxx의 갱신을 위해 total 에 금을 찾은 위치를 더한 금을 넣어준다
                               # 이후 다시 max를 통해 비교
                                q.append((nr, nc, path + [(nr, nc)], total + grid[nr][nc]))
                    # 현재까지의 최대값으로 후에 최종적으로 갱신
                    greatest = max(maxx, greatest)
        return greatest
