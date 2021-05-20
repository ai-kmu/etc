class Solution:
    def myAtoi(self, str: str) -> int:
        number = ''
        for char in str:
            try:                                          
                if char in [' ', '+', '-']:               # ' ', '+', '-'가 숫자 앞에 나올 수 있기 때문에 먼저 처리
                    if number == '':
                        if char == ' ':                   # 공백은 continue
                            continue
                        elif char == '+' or char == '-':  # '+', '-'는 number에 저장
                            number = char     
                    else:                                 # 이미 nmumber에 저장된 값이 있는 경우에는 break
                        break 
                else:                                     # 숫자인 경우에는 number에 저장
                    int(char)                             # int[char]에 경우, 오류가 날 수 있기 때문에 try, except 구문 사용
                    number += char
            except:                                       # 오류가 발생한 경우, break
                break     
        if number in ['', '-', '+']:                      # 숫자가 없는 경우, 0 반환
            return 0
        if int(number) < -2**31:                          # 음수인 경우, -2**31보다 작은 경우
            return -2**31
        elif int(number) > 2**31 - 1:                     # 양수인 경우, 2**31 - 1보다 큰 경우
            return 2**31 - 1
        else:                                             # 나머지는 그대로 
            return int(number)
