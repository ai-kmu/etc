class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        if N==1:                                        # 크기 1이면 바로 리턴
            return
        
        lines = [matrix[i] for i in range(N-1,-1,-1)]   # 매트릭스 행 뒤집기
        matrix[::] = list(map(list,zip(*lines)))        # 매트릭스 재조합
