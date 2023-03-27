class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        
        tmp = []
        # 걍 돌면서 추가
        for i in matrix:
            for j in i:
                tmp.append(j)
        # 정렬
        tmp.sort()
        # 인덱스 맞춰서 리
        return tmp[k-1]
