class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        cnt = 0
        coins_left = coins
        for elem in costs:
            coins_left -= elem
            if coins_left < 0:
                break
            else:
                cnt += 1
        return cnt
        
