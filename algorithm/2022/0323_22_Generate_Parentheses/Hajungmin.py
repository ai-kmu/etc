class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        # 괄호들을 담아둘 stack을 하나 선언한다.
        stack = []
        ans = []
        
        # backtrack 알고리즘을 사용하여 완전탐색에서 연산량을 줄여준다.
        # start는 여는 괄호의 개수, end는 닫는 괄호의 개수
        # 따라서 조합을 다 마쳤을 때, start와 end는 각각 n개씩 존재해야한다.
        def backtrack(start, end):
            # 만약 여는 괄호, 닫는 괄호, 괄호의 개수가 같다면 stack에 해당 조합을 더해줌 
            if start == end == n:
                ans.append("".join(stack))
                return
            
            # 여는 괄호가 n보다 작을 경우 여는 괄호를 하나 넣고 여는 괄호 개수를 하나 늘려준다.
            # 그리고 start를 1 늘려서 함수를 호출한다.
            # 만약 앞선 경우를 전부 고려했다면 이후 stack에서 pop을 통해 요소를 제거한다.
            if start < n :
                stack.append("(")
                backtrack(start + 1, end)
                stack.pop()
            
            # 닫는 괄호가 여는 괄호보다 작으면 닫는 괄호 개수를 하나 늘려준다.
            # 이후 end를 1 늘려서 함수를 호출한다.
            if end < start:
                stack.append(")")
                backtrack(start, end + 1)
                stack.pop()
        
        # 0,0부터 시작한다.
        backtrack(0,0)
        return ans
