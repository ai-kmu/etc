from collections import deque
class Solution:
    def decodeString(self, s: str) -> str:
        string_stack = [] # 현재 int와 그에 해당되는 string 저장하기 위한 stack
        now_string=[] # 현재 string
        current_int = 0
        for ch in s:
            if ch == "[": # '['가 나오면 현재 string에 해당되는 int를 stack에 저장한 후 현재 string과 현재 int 초기화
                string_stack.append((now_string, current_int))
                now_string = []
                current_int = 0
            elif ch == "]": # ']'가 나오면 stack에서 나중에 저장한 string과 int를 불러와서 now_string을 업데이트
                s, i = string_stack.pop()
                now_string = s + i * now_string
            elif ch in "0123456789": # 숫자가 나오면 자리수에 맞게 현재 int 갱신
                current_int = current_int * 10 + int(ch)
            else: # 나머지 영어 철자는 now_string에 저장
                now_string.append(ch)
        return "".join(now_string)
