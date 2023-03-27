# 
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        mok = k // n
        nameogi = k % n
        a = []
        if k == 1:
            return matrix[0][0]
        if mok == 0:
            return matrix[0][nameogi]
        for _ in matrix:
            for i in range(mok+1):
                a.append(_[i])
        print(a)
        return a[nameogi]
