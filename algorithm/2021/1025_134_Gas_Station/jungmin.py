class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0 # 시작 지점 초기화
        r = 0 # 총 필요한 최소 기름 양
        tank = 0 # 탱크에 있는 기름 양
        
        # 첫 지점 부터 gas-cost를 계산하여 사용하고 남은 기름 양을 계산한다.
        # 현 지점에서 연료를 사용하고 남는 기름 양 tank 계산하여 누적
        # tank 누적값이 음수인 순간 그 양만큼 r에 저장하여 필요한 최소 기름양을 누적해서 더하도록 한다.
        # 그리고 시작 지점을 다음으로 넘어가서 또 확인하도록 한다.
        for i in range(len(gas)):
            tank += (gas[i] - cost[i]) 
            if tank < 0: 
                r -= tank
                start=i+1
                tank=0
                
        if tank >= r: # for 반복문을 다 돈 후 남아 있는 tank가 최소 필요한 양 r보다 크면 마지막으로 갱신한 시작 지점을 return
            return start
        
        else: # 최종 tank가 r보다 작으면 순회할 수 없다는 의미이므로 -1 출력
            return -1
