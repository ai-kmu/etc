class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def search_correct(pare):
            stk=0
            res=[]
            for ps in pare:
                for p in ps:
                    if p=='(':
                        stk+=1
                    else:
                        stk-=1
                    
                    if stk<0:
                        break;
                
                if stk==0:
                    res.append(ps)
                
                stk=0
            return res
        
        parentheses=[]
        
        for b in range(2**(2*n-1),2**(2*n)):
            par=''
            b_str=format(b,'b')
            for s in b_str:
                if s=='1':
                    par+='('
                else:
                    par+=')'
                    
            parentheses.append(par)

        output=search_correct(parentheses)
        
        return output
