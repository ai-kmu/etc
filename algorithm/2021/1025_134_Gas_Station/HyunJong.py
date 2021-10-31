## 아이디어 1 : 한바퀴를 도는게 가능한지를 보는 문제이다. -> 차가 전부를 다 가야하므로 gas 총량이 소모총량보다 많아야 한다.
## 아이디어 2 : 한바퀴 돌 때 방향이 정해져 있다 -> 주어진 벡터를 순차적으로 돌았을 때 가능한 시작점이면 무조건 누적값이 양수가 나올 것이다.
    ## 왜냐하면 순차적으로 더했을 때 누적된 값이 음수가 되는 건 탱크에 있는 gas보다 소모량이 더 크다는 의미이고 양수로 유지되는 건 아직 탱크에 있는 gas가 소모량보다 더 많다는 의미이고 
    ## 이는 차가 계속 돌아갈 수 있다는 것을 의미하기 때문이다.
## 아이디어 3 : 문제에서 시작점은 고유하다는 것을 보장했으므로 가능한 시작점만 나오면 된다.

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        gas_sum, cost_sum = 0, 0
        for i in range(len(gas)): ## 아이디어 1
            gas_sum += gas[i]
            cost_sum += cost[i]
            
        if cost_sum > gas_sum:  ## 당연히 안 되는 경우, 가능한 경우는 무조건 gas 양이 소모량보다 커야 한다.
            return -1

        sum, start = 0, 0 
        for i in range(len(gas)): ## 아이디어 2
            sum += gas[i%len(gas)] - cost[i%len(gas)] ## 누적값 파악 : 탱크에 있는 gas 잔량
            if sum < 0: ## 음수이면
                sum = 0 
                start = i + 1 ##아이디어 3  시작 포인트를 다음칸으로 옮겨준다.
                
        if start > len(gas): ## 만약 start 포인트가 인덱스 범위를 초과하면 가능한 경우가 없다는 의미이다. 
            return -1 
        else :
            return start 
