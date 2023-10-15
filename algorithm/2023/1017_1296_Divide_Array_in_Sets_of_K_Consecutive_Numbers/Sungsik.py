from collections import Counter


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False
        
        # 효율성을 위해 counter 사용
        counter = [list(x) for x in sorted(Counter(nums).items())]
        remained = len(nums)
        
        while remained > 0:
            # 현재 최솟값과 그 index를 찾음
            for i, (val, count) in enumerate(counter):
                if count == 0:
                    continue
                else:
                    min_val, min_idx = val, i
                    counter[i][1] -= 1
                    break
            
            # 그 뒤의 k-1 번째가 연속된 숫자이며, count를 다 쓰지 않았음을 확인
            for i in range(1, k):
                try:
                    val, count = counter[min_idx+i]
                except IndexError:
                    return False
                if val != min_val + i or count == 0:
                    return False
                counter[min_idx+i][1] -= 1
            remained -= k
            
        return True
