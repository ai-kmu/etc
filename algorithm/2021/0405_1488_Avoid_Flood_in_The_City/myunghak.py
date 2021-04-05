# dictionary를 이용해 각 lake가 처음 나온 index를 저장하고
# 거기서부터 다시 나온곳 까지 한번이라도 비가 안왔으면 비가 안온 구역을 채워주고 넘어감
# 비간 안온적이 없으면 return []

import numpy as np

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        ans = np.full(len(rains),-3)
        lake = {}
        
        empty_idx = []
        
        for i, r in enumerate(rains):
            if r == 0:
                pass
            else:
                if r in lake:
                    try:
                        idx = np.where(ans[lake[r]:i] == -3)[0][0]
                    except:
                        return []
                    if idx > 0:
                        idx += lake[r]
                        ans[idx] = r
                    else:
                        return []
                    lake[r] = i
                    
                else:
                    lake[r] = i
                ans[i] = -1
                
                
        for i in range(len(ans)):
            if ans[i] == -3:
                ans[i] = 1
                
        
        return ans
        
