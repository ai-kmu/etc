import heapq


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # heap을 사용하여 최솟값을 순회
        heap = [(matrix[0][0], 0, 0)]
        visited = set(((0, 0)))
        
        count = 1
        n = len(matrix)
        
        while count < k:
            # heappop을 하여 count번째 작은 값을 뽑음
            num, row, col = heapq.heappop(heap)
            # 아래와 오른쪽을 방문하지 않은 경우 heap에 추가
            if row < n - 1 and (row+1, col) not in visited:
                visited.add((row+1, col))
                heapq.heappush(heap, (matrix[row+1][col], row+1, col))
            if col < n - 1 and (row, col+1) not in visited:
                visited.add((row, col+1))
                heapq.heappush(heap, (matrix[row][col+1], row, col+1))
            count += 1
        
        return heapq.heappop(heap)[0]
