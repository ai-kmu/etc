from collections import deque

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        que = deque()
        answer = []
        def par_func(open_p, close_p):
            if (open_p == close_p == n):
                answer.append(''.join(que))
            
            if open_p < n:  # n보다 작으면 (를 넣고
                que.append("(")
                par_func(open_p + 1, close_p)
                que.pop()
             
            if close_p < open_p:    # 열려잇는 괄호보다 작으면 닫아줘야 함
                que.append(")")
                par_func(open_p, close_p + 1)
                que.pop()
                
        par_func(0, 0)
        return answer
