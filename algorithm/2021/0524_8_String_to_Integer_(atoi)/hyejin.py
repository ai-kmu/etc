class Solution:
    def myAtoi(self, s: str) -> int:
        digit = ''
        sign = ''
        for char in s:
            if char == "+" or char == "-": # sign 부호 결정
                if digit == "":
                    sign += char
                else:
                    break
            elif char == " " and digit == "" and sign == "": # whitespace 제거
                continue
            elif char.isdigit(): # 만약 숫자면 추가
                digit += char
            else: # alphabet일때
                if digit != '': # digit이 있으면 중단
                    break
                else: # 없는 상태면 0 반환
                    return 0

        if digit == '': # digit이 비어있을 떄
            return 0
        
        if sign == '-': 
            return max(-(2**31), -(int(digit)))
        elif sign == '+' or sign == '':
            return min(2**31-1, int(digit))
        else: # sign이 +- 두개 다 있을 때
            return 0
