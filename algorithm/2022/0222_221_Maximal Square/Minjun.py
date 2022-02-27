class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        '''
        m,n >= 1 -> 1   m,n -> m,n**2
        m,n >= 2 -> 4   m,n**2
        m,n >= 3 -> 9   m,n**2
        ==> m,n 일 때 가능한 최대 정사각형은 min(m,n)**2
        '''
        m, n = len(matrix), len(matrix[0])
        
        a = min(m,n)
        
        
    def findMax(self, a):
        '''
        a 정사각형 가능한 최대 값 -> a**2
        a-1 -> a-1**2
        a-2 -> a-2**2
        a-a+1 -> 1
        '''
        
        for i in range a:
            matrix[m-i][n-i]
        
