'''
오답코드
'''
from collections import deque


class Solution:
    def checkValidString(self, s: str) -> bool:
        
        # s의 길이가 1인 경우 처리
        if len(s) == 1:
            if s == '*':
                return True
            else:
                return False
            
        stk = []
        cnt = 0

        for i in s:
            if i == '(':
                stk.append(i)
            elif i == ')':
                if stk:
                    stk.pop()
                else:
                    stk.append(i)
            elif i == '*':
                if stk:
                    stk.pop()
                cnt += 1

        if cnt >= len(stk):
            return True
        
        if len(stk) == 0:
            return True
            
        else:
            return False
