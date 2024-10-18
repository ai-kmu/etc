class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)

        idx, ans = 0, 0
        
        for child in g:
            if idx == len(s):
                break
            if s[idx] >= child:
                ans += 1
                idx += 1

        return ans
