class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        s_idx = 0
        ans = 0
        for i in g:
            try:
                while s[s_idx] < i:
                    s_idx += 1
                ans += 1
                s_idx += 1
            except:
                break
        return ans
