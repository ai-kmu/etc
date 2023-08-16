# 솔루션 참고
class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:

        ans = 0
        n//=2                                               # 부모 node만 반복하면 되므로

        for i in reversed(range(n)):
        
            mn, mx = sorted((cost[2*i+1], cost[2*i+2]))    # 자식 node중 min, max 구해서

            ans += mx - mn
            cost[i] += mx

        return ans
