class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        
        stack = []
        res = []
        
        # 해를 하나씩 내려가면서 구한다. 
        # 더이상 만들 수 없을 때 돌아가는 recursive한 특징을 가지고 있다. 
        
        
        
        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack)) #가지가 끝나는 부분이다. res에 append를 해주면서 전에 하던 시점으로 돌아간다. 
                return
                
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop() #backtracking을 위해 마지막의 바로직전의 경우에 pop()을 수행한다. 
                
            if closedN < openN: #) 가 (보다 작으면 소괄호 추가
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
                
        backtrack(0, 0)
        return res
