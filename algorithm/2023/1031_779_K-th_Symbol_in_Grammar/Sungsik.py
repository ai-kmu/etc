class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        '''
        0
        0 1
        0 1 1 0
        규칙 : binary tree로 고려하고, 
              k 값에 의해 왼쪽으로 갈지, 오른쪽으로 갈지 결정
              오른쪽으로 갈 경우 bit를 flop
        '''
        bit = 0
        
        for i in range(n-2, -1, -1):
            if k > 2 ** i:
                k -= 2 ** i
                bit = 1 - bit
        
        return bit
