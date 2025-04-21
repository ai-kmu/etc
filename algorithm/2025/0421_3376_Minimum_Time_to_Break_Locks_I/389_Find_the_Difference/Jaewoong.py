class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_sorted = sorted(s)
        t_sorted = sorted(t)
        
        for a, b in zip(s_sorted, t_sorted):
            if a != b:
                return b
        return t_sorted[-1]
        
