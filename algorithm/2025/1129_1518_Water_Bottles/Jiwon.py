class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        # 교환 불가능한 경우
        if numBottles < numExchange:
            return numBottles

        # 일단 처음 거는 다 마심 -> 공병
        ans = numBottles

        # 바꿀 수 있는 병의 개수가 교환 개수보다 클 동안은 계속 진행
        while numBottles >= numExchange:
            exchange = numBottles // numExchange
            ans += exchange
            # 새로 바꾼 병 + (남은 공병)
            numBottles = exchange + (numBottles % numExchange)

        return ans
