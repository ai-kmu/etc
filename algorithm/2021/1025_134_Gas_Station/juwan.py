class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas) # gas station의 수
        sum = 0 # 총합
        min = 10**4 # 일단 cost 또는 gas 의 양이 10**4까지임.
        idx = -1
        for i in range(n): # 어차피 1 cycle을 돌아야하는데, 1 cycle을 돌려면 전체를 순회함.
                           # 따라서 어디서부터 시작을 하여도 그 gas를 채우는 것과 비용은 같아짐.
                           # 결론 : 시작점을 고려하지 않아도 된다는 것.
            sum += gas[i] - cost[i]
            # 그 station에 가는 비용은 어차피 해당 station에 도착하면 채워짐
            if sum < min:
              # 즉, 다음 지역으로 이동할 때의 드는 비용보다 현재 station의 기름이 더 많다면
              # 최소값이 더 이상 변하지 않을 것.
              # 하지만 이후에도 최소값은 언제든지 갱신될 수 있다.
                min = sum
                idx = i
        # 최소값은 언제든지 갱신이 될 수 있지만, 결국에 전체 for loop 이후에도 sum 값이 0을 넘지 못한다면
        # 어디서부터 출발을 하여도 순환할 수 없다는 것.
        if sum >= 0:
            return (idx + 1) % n
        # idx는 start 인덱스 이전의 station이 저장된다. 
        # 그 이유는 start 인덱스에서는 min값이 더 이상 갱신되지 않는 것인데, idx에는 min 값이 갱신되어야만
        # 저장이 된다. 따라서 idx는 start 인덱스 바로 이전.
        # n이 없다면 sample case는 된다. 하지만 submit에는 오류가 난다. 아마 답이 맨 마지막 idx이기 때문에
        # 배열에서 없는 값을 찾아오기 때문이다. 따라서 간단히 % n으로 맞춰준다.
        
        
        
        else:
            return -1
          
        
