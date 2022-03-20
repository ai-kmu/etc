class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        stack = [] # 하나의 string에 저장할 소괄호 모임 저장(stack 방식)
        ans = [] # 정답 저장
        
        # backtracking 알고리즘 적용
        # 해를 찾는 도중 그 경로가 해를 못찾을 것 같으면 다시 경로를 되돌아 간다.
        # o: 여는 소괄호 번호
        # c: 닫는 소괄호 번호
        def bt(o,c):
            # 여는 소괄호 갯수와 닫는 소괄호 갯수가 같으면 함수 끝냄
            if o == c == n:
                ans.append("".join(stack))
                return 
            # o가 n보다 작으면 여는 소괄호 추가
            if o < n:
                stack.append("(")
                bt(o+1, c)
                stack.pop() # backtracking을 하기 위해 stack에서 몇 요소를 pop하도록 한다.
            # c가 o보다 작으면 닫는 소괄호 추가
            if c < o:
                stack.append(")")
                bt(o, c+1)
                stack.pop() # backtracking을 하기 위해 stack에서 몇 요소를 pop하도록 한다.
        bt(0,0)
        return ans
