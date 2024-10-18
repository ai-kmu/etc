class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        g_ = [False] * len(s)
        s_ = [False] * len(s)
        cnt = 0

        if not s:
            return 0
            
        if min(g) > max(s):
            return 0

        for idx_, i in enumerate(g):
            for idx, j in enumerate(s):
                # print(j, i)
                
                if j >= i:
                    if s_[idx] == False and g_[idx_] == False:
                        # print(j, i)
                        cnt += 1
                        s_[idx] = True
                        g_[idx_] = True

        return cnt
