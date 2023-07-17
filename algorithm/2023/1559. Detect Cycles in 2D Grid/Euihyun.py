# 못풀었습니다. 리뷰 안해주셔도 돼요
from collections import deque

class Solution(object):
    def containsCycle(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        m, n = len(grid), len(grid[0])
        
        # 가능한 이동 방향 정의
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        # 방문한 위치를 추적하는 2차원 배열
        seen = [[False] * n for _ in range(m)]
        
        # 간단한 BFS를 사용하여 사이클 검사
        def bfs(r, c):
            # 현재 위치와 이전 위치를 추적하는 큐를 초기화
            queue = deque([((r, c), (-1, -1))])
            
            # 현재 위치의 값 저장
            value = grid[r][c]
            seen[r][c] = True
            
            # BFS를 통해 그리드를 탐색
            while queue:
                current_position, prev_position = queue.popleft()
                
                # 가능한 이동 방향 탐색
                for dr, dc in directions:
                    new_r = current_position[0] + dr
                    new_c = current_position[1] + dc
                    
                    # 새로운 위치가 유효하고 이전 위치와 다르며, 같은 값인 경우
                    if new_r >= 0 and new_r < m and new_c >= 0 and new_c < n and \
                       grid[new_r][new_c] == value and (new_r, new_c) != prev_position:
                        
                        # 이미 방문한 적이 있는 위치라면 사이클이 존재함
                        if seen[new_r][new_c]:
                            return True
                        
                        # 그렇지 않은 경우 큐에 새로운 위치 추가하고 방문했다고 표시
                        queue.append(((new_r, new_c), current_position))
                        seen[new_r][new_c] = True
                        
            return False
        
        # 모든 셀에 대해 반복하여 사이클 검사
        for r in range(m):
            for c in range(n):
                # 방문하지 않은 셀에 대해서만 검사를 수행
                if not seen[r][c] and bfs(r, c):
                    return True
                
        return False
