# flatten 한다음 sorting
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        return sorted([item for sublist in matrix for item in sublist])[k-1]
