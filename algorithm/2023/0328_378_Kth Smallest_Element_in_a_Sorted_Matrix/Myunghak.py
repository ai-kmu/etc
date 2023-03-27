# # flatten 한다음 sorting
# class Solution:
#     def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
#         return sorted([item for sublist in matrix for item in sublist])[k-1]


# directed graphg의 BFS
# n*n크기를 matrix에서 (x,y)가 rank r이 될 수 있는 조건은 아래와 같다.
# x(n+1) + y(n+1) -xy - 2n < r < xy
# 이 떄 n값과 r값은 상수이므로 부등식을 방정식으로 바꾸어 x,y쌍의 해를 구하면 가능한 부분만 BFS로 탐색이 가능하다.
# 그런데 솔직히 sorting이 더 빠른듯...

import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        
        visited = set()
        start_index = 0
        pq = []
        for x in range(1,n+1):
            y = max(int((k + 2 * n - x * (n+1)) / (n+1 - x) - 1e-10), 0)
            
            start_index += y
            if y < n:
                visited.add((x-1, y))
                heapq.heappush(pq, [matrix[x-1][y], x-1, y])
        
        for i in range(start_index, k):
            v, r, c = heapq.heappop(pq)

            if r + 1 < m and (r + 1, c) not in visited:
                heapq.heappush(pq, [matrix[r + 1][c], r + 1, c])
                visited.add((r + 1, c))

            if c + 1 < n and (r, c + 1) not in visited:
                heapq.heappush(pq, [matrix[r][c + 1], r, c + 1])
                visited.add((r, c + 1))

        return v
