class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 가능한 모든 괄호를 만들고, 그중에서 올바른 괄호쌍만 골라낸다.
        def search_correct(pare): # 올바른 괄호 찾기
            stk=0 # stack을 이용해 stack에 (의 갯수가 0보다 작아지면 틀리다고 판단
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
        
        for b in range(2**(2*n-1),2**(2*n)): # n쌍의 크기를 가지는 괄호 만들기
            par=''
            b_str=format(b,'b') # 숫자를 이진화시켜 1이면 (, 0이면 ) 로 치환
            for s in b_str:
                if s=='1':
                    par+='('
                else:
                    par+=')'
                    
            parentheses.append(par)

        output=search_correct(parentheses)
        
        return output
