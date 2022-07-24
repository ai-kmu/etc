class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        ans = []
        dict = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        
        if len(digits) == 0:
            return []
        
        # 글자 하나씩 우선 넣어줌
        ans=list(dict[digits[0]])
        
        for i in range(1,len(digits)):
            temp=[]
            for ch in dict[digits[i]]:
                for j in ans:
                    # ans에 있던 값들 뒤에 붙여준다 
                    temp.append(j+ch)
            ans = temp
            
        return ans
        
