class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) <= 0 and len(t) >= 0:
            return True

        current_idx = 0
        next_ch = s[current_idx]
        for elem_s in t:
            
            if elem_s == next_ch:
                if len(s) - 1 == current_idx:
                    return True

                current_idx += 1
                next_ch = s[current_idx]
            
        return False
