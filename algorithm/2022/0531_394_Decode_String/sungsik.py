from collections import deque

class Solution:
    def decodeString(self, s: str) -> str:
        answer = ""
        stack = deque()
        
        for c in s:
            # 만약 ]를 마주칠 경우
            if c == "]":
                # []안에 있는 모든 string을 가져옴
                tmp_str = ""
                while True:
                    tmp_c = stack.pop()
                    if tmp_c == "[":
                        break
                    else:
                        tmp_str = tmp_c + tmp_str
                
                # 반복되는 횟수를 가져옴
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                num = int(num)
                
                # 반복시킨 후 stack에 다시 집어넣음
                stack.append(tmp_str * num)
                
            else:
                stack.append(c)
        
        return "".join(stack)
                
            
            
