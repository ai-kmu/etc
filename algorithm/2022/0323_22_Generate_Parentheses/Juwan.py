class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        if n == 1:
            return ["()"]
        
        ans = set()
        
        for i in self.generateParenthesis(n-1):
            print(i)
            for j in range(len(i)):
                print(j)
                ans.add(i[0:j+1]+"()"+i[j+1:len(i)])
        ans = list(ans)
        return ans


        
        
        
