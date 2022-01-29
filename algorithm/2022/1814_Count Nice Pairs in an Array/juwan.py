from collections import defaultdict

def rev(num):
    
    return int(str(num)[::-1])

M = 10**9+7

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        
        mapping = defaultdict(int)
        
        for num in nums:
            mapping[num-rev(num)] += 1
        
        cnt = 0
        
        for v in mapping.values():
            cnt = cnt + v*(v-1)//2
        
        return cnt%M
