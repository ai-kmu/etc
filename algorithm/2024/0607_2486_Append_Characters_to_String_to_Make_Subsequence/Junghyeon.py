class Solution:
    def appendCharacters(self, s, t):
        if t in s:
            return 0
        
        idx = 0
        for i in s:
            if t[idx] == i:
                idx += 1

        result = len(t) - idx
        
        return result
