# 솔루션 참고. 풀이 안해주셔도 됩니다


class Solution:
    def maxBalancedSubarray(self, nums: List[int]) -> int:

        states = defaultdict(int)
        cur_state, ans = (0, 0), 0
        states[cur_state] = -1

        for idx, num in enumerate(nums):
            xor_, evn_odd = cur_state
            cur_state = (xor_^ num, evn_odd + 2 * (num%2) - 1)
            
            if cur_state not in states:
                states[cur_state] = idx
            else:
                span = idx - states[cur_state]
                if span > ans: ans = span
                
        return ans
    
