# time limit exceed code
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:        
        
        if sum(gas) < sum(cost):
            return -1
            
        l = len(gas)
        if l == 1 and gas[0] >= cost[0]:
            return 0
            
        init_list = []
        for i in range(l):
            if (gas[i] - cost[i]) > 0:
                init_list.append((i, gas[i] - cost[i]))
        init_list.sort(reverse=True, key=lambda x:x[1])
        
        
        # print(init_list)
        while init_list:
            init_idx, _ = init_list.pop()
            cur = init_idx
            cur_gas = gas[cur]
            for _ in range(l):
                # print(cur, cur_gas)
                cur += 1
                if cur == l:
                    cur = 0
                if (cur_gas - cost[cur - 1]) < 0 :
                    break
                cur_gas += (gas[cur] - cost[cur - 1])
                if cur == init_idx:
                    return init_idx

        return -1

# 정답 코드
'''
핵심 키포인트 1 : gas의 양이 cost의 양보다 많으면 해는 반드시 존재하고 unique하다.
핵심 키포인트 2 : 특정 idx a에서 시작했을 때 idx b에서 가스가 부족하다면, 해는 a와 b 사이에서는 존재하지 않는다.
'''

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:        

        # 해가 존재하는지 확인
        if sum(gas) - sum(cost) < 0:
            return -1

        # tank에 남은 기름의 양과 정답 idx 초기화
        res, ans = 0, 0
        for i, (v1, v2) in enumerate(zip(gas, cost)):
            res += (v1 - v2)

            # gas의 양이 부족하면 바로 뒤 idx가 정답이라 가정하고 다시 수행
            if res < 0:
                ans = i + 1
                res = 0
        
        return ans
