### Time out

from collections import defaultdict, deque

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        dic = defaultdict(int)                            
        multi = set()
        for i in rains:       # 여러번 비가 내리는 lake 체크
            dic[i] += 1
            if dic[i]>1:
                multi.add(i)         
                
        ans = []
        dic3 = defaultdict(int)   # lake의 현재 상태
        for idx, i in enumerate(rains): 
            if i==0:
                tag = 0
                for j in range(idx+1, len(rains)):      # dry할때, 가장 가까운 중복되어 내리는 lake를 선택
                    temp_idx = rains[j]
                    if temp_idx in multi and dic3[temp_idx]==1:
                        dic3[temp_idx] = 0
                        ans.append(temp_idx)
                        tag = 1
                        break
                if tag==0:
                    dic3[1] = 0
                    ans.append(1)
                continue
            elif i>0:
                if dic3[i]==0:
                    dic3[i] = 1
                    ans.append(-1)
                else:
                    print(ans)
                    return []
        return ans
