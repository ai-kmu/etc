# dp로 품
# sliding window를 만듦
# slding window에 idx 0부터 차례로 집어 넣음
# sliding window내의 크기가 음수가 되면 양수가 될때 까지 맨 왼쪽것을 하나 뺌
# slinding window의 크기가 입력값의 크기와 같아지면 반환
# 위 조건을 만족하지 못하면 return -1


class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:
        benefit = [gas[i] - cost[i] for i in range(len(gas))]  # 각 주유소에서 얻을 수 있는 이득 = 현재 주요소에서 체울 수 있는 가스 - 다음 도시까지 드는 가스
        benefit += benefit[:-1]  # 순환해야 하므로 뒤에 더 붙여 줌
        
        window_size, sum_ = 0, 0
        
        for i in range(len(benefit)):
            sum_ += benefit[i]
            window_size+=1
            
            while(sum_<0): # 음수면 양수 될때 까지 앞에거 뺌
                sum_ -= benefit[i-window_size+1]
                window_size-=1

            if window_size == len(gas): # sliding window의 크기가 입력값의 크기와 같아지면 반환
                return i-window_size+1

        return -1
        
