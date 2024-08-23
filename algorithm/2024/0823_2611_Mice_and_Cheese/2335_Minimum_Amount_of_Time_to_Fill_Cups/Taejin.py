class Solution:
    def fillCups(self, amount: List[int]) -> int:
        cnt = 0
        amount.sort(reverse=True)

        while amount[0] > 0:
            amount[0] -= 1
            amount[1] -= 1
            amount.sort(reverse=True)
            cnt += 1
        
        return cnt
