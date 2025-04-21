class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if s == "":
            return t
        
        s_cnt = Counter(s)
        t_cnt = Counter(t)

        d = t_cnt - s_cnt
        
        for key in d.keys():
            return key
