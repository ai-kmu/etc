class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
        num = 0
        tmp = sorted(piles)
        
        for i in range(len(piles) // 3):
            tmp.pop()
            num += tmp.pop()
        
        return num
