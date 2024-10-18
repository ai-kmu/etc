class Solution(object):
    def findContentChildren(self, g, s):
        # g가 사람
        # s가 쿠키
        g.sort()
        s.sort()
        point = 0
        num = 0
        for i in range(len(s)):
            if len(g) > point:
                if s[i] >= g[point]:
                    point += 1
                    num += 1    
        return num
