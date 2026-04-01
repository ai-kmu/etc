# 솔루션 참고
# Permutation
from itertools import permutations

class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        zero_idx = []
        extra_stones = []

        for i in range(3):
            for j in range(3):
                if grid[i][j] == 0:
                    zero_idx.append((i, j))
                elif grid[i][j] > 1:
                    for _ in range(grid[i][j] - 1):
                        extra_stones.append((i, j))

        min_total_dist = float('inf')

        for p in permutations(extra_stones):
            current_dist = 0
            for i in range(len(zero_idx)):
                dist = abs(zero_idx[i][0] - p[i][0]) + abs(zero_idx[i][1] - p[i][1])
                current_dist += dist
            
            min_total_dist = min(min_total_dist, current_dist)

        return min_total_dist
