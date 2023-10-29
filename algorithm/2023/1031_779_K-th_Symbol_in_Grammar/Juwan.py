class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # n개의 row가 주어졌을 때, 바로 직전 값이 0이면 01로, 1이면 10으로 변환하는 코드.
        #1st 0
        #2nd 10
        #3rd 0110
        #4th 0110 1001
        #5th 0110 1001 1001 0110
        #6th 0110 1001 1001 0110 1001 0110 0110 1001
        
        
        if n == 1:
            return 0
        
        half = pow(2, n - 2)

        if k <= half:
            return self.kthGrammar(n-1, k)
        else:
            return 1 - self.kthGrammar(n-1, k - half)
