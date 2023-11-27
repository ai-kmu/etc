# test만 통과하고 정답 봤습니다. 리뷰 안해주셔도 됩니다.

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # gas의 총합에서 cost의 총합을 뺀 결과가 음수면 불가능한 경우 -1을 반환
        if (sum(gas) - sum(cost) < 0):
            return -1
        
        # gas 탱크와 출발 인덱스를 초기화
        gas_tank, start_index = 0, 0
        
        # 모든 주유소를 순회하면서 가스 탱크의 상태를 업데이트
        for i in range(len(gas)):
            gas_tank += gas[i] - cost[i]
            
            # 가스 탱크가 음수가 되면 이전 인덱스에서 다시 출발
            if gas_tank < 0:
                start_index = i + 1
                gas_tank = 0
            
        return start_index
