class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = [] # 요소 index stack 방식으로 저장
        stars = [] # *의 인덱스 저장
        
        ```
        '('는 stack에 바로 append
        '*'는 stars에 append
        ')'의 경우 경우에 따라 다르게 수행
        ```
        for i, v in enumerate(s):
            if v == '(':
                stack.append(i)
            elif v == ')':
                if stack: 
                    stack.pop(-1) # stack에 있는거 마지막 요소 제거
                elif stars:
                    stars.pop(-1) # stars에 있는거 마지막 요소 제거
                else:
                    return False # stack stars 둘 다 비어있으면 바로 false return
            else:
                stars.append(i)
        
        ```
        '('는 '*'보다 뒤에 있어야 한다. 하나라도 그렇지 않으면 invalid하므로 false return
        ```
        while stack and stars:
            if stack[-1] > stars[-1]:
                return False

            stack.pop(-1)
            stars.pop(-1)
        
        ```
        stack에 남는게 있으면 false return, 그렇지 않으면 true return
        ```
        if stack:
            return False
        else:
            return True
