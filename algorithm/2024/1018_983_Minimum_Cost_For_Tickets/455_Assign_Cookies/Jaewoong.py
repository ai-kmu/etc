class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        i = 0
        j = 0
        while i < len(g):
            while j < len(s) and s[j] < g[i]:
                j += 1
            if j == len(s):
                break
            i += 1
            j += 1
        
        return i        
