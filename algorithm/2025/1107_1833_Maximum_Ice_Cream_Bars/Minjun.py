class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        tmp = 0
        cnt = 0
        for i in sorted(costs):
            tmp += i
            if tmp > coins:
                return cnt
            cnt += 1
        return cnt
