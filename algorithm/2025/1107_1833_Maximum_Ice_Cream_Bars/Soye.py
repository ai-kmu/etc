# 솔루션 참고해서 풀이 괜찮아용
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs = sorted(costs)
        ans = 0
        for i in range(len(costs)):
            if coins >0 and coins >= costs[i]:
                coins -= costs[i] 
                ans+=1
        return ans
