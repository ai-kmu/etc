# flatten 한다음 sorting
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        matrix2 = []
        for m in matrix:
            matrix2 += m
        return sorted(matrix2)[k-1]
