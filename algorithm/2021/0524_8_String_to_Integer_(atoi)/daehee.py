class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()                  # 공백 제거
        
        if len(s)==0:
            return 0
        str_int = ''
        
        sign = 1                        # 부호 확인
        if s[0]=='+':
            sign = 1
            s = s[1:]
        elif s[0]=='-':
            sign = -1
            s = s[1:]
            
        if len(s)==0:
            return 0
        
        for c in s:                     # 왼쪽부터 돌아가면서 숫자면 붙여주기
            if c.isnumeric():
                str_int += c
            else:
                if len(str_int)==0:
                    return 0
                break
        
        integer = sign*int(str_int)      # 자릿수 계산
        if -2**31 > integer:                
            integer = -2**31
        elif integer > 2**31-1:
            integer = 2**31-1
        return integer
