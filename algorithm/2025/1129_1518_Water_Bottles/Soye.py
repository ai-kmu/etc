# 솔루션 참고했습니다
# 풀이 안 대주셔도 돼요
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        filled = 0
        empty = 0
        ans = numBottles

        while numBottles >= numExchange:
            filled = numBottles//numExchange
            ans += filled
            empty = numBottles % numExchange
            numBottles = filled + empty

        return ans
            
        
