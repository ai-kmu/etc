from collections import Counter
from collections import deque

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        
        # 나누어 떨어지지 않는경우
        if len(nums) % k != 0:
            return False

        c_dict = Counter(nums)      
        keys = sorted(list(c_dict.keys()))
        deq = deque(keys)

        while deq:
            prv_key = deq[0]
            prv_val = c_dict[deq[0]]
            remove_num = c_dict[deq[0]]
            deq.popleft()

            # 탐색할 개수가 안되면 return False
            if len(deq) < k-1:
                return False
            # k 수만큼 탐색
            for i in range(k-1):
            
                cur_key = deq[i]
                cur_val = c_dict[deq[i]]

                # key가 연속적이지 않고, key 숫자가 더 적어서 연속으로 못하는경우 return False
                if prv_key + 1 != cur_key or prv_val > cur_val:
                    return False

                c_dict[cur_key] -= remove_num
                prv_key, prv_val  = cur_key, cur_val

            # 개수가 0인것 제외
            while deq and c_dict[deq[0]] == 0:
                deq.popleft()
        
        return True
