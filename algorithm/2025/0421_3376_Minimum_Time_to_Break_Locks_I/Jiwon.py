# 솔루션 참고

class Solution:
    def findMinimumTime(self, strength: List[int], K: int) -> int:
        s = tuple(sorted(strength))
        
        @cache
        def dp(state, x):
            if len(state) == 0:
                return 0
            
            result = float('inf')
            for i, s in enumerate(state):
                minutes = (s + x - 1) // x
                new_state = state[:i] + state[i + 1:]
                current = minutes + dp(new_state, x + K)
                result = min(result, current)
            return result

        return dp(s, 1)
