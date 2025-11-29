class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        # 현재까지 마신 물병 수 (초기에는 모두 마신다고 가정)
        total_drunk = numBottles
        
        # 현재 가지고 있는 빈 병 수
        empty_bottles = numBottles
        
        # 빈 병을 계속 교환할 수 있는 동안 반복
        while empty_bottles >= numExchange:
            # 교환으로 얻을 수 있는 새 물병 수
            new_bottles = empty_bottles // numExchange
            
            # 마신 물병 수 추가
            total_drunk += new_bottles
            
            # 마신 새 물병은 다시 빈 병으로 바뀜
            empty_bottles = (empty_bottles % numExchange) + new_bottles
        
        return total_drunk
