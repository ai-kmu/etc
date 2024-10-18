class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        cnt = 0
        
        # 7 8 9 10
        # 5 6 7 8 
        i_l=0
        i_r=0
        while True:
            if i_l == len(g) or i_r == len(s):
                break
            if g[i_l] <= s[i_r]:
                print(g[i_l], s[i_r])
                cnt = cnt + 1
                i_r= i_r+1
                i_l= i_l+1
            else:
                print(s[i_r])
                i_r= i_r+1
            


        return cnt

