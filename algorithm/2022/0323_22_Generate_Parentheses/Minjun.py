class Solution:
    # 재귀
    def generate(self, left, right, s, ans):
        if(left == 0 and right == 0):
            ans.append(s)
            return 
        if(left > 0):
            self.generate(left-1, right, s+"(", ans)
        if(left<right):
            self.generate(left, right-1, s+")", ans)
            

    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.generate(n,n,"",ans)
        return ans 
