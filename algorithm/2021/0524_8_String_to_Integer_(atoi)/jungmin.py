class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip() # 빈칸 제거
        max_int = 2**31 - 1 # 최대
        min_int = -2**31 # 최소
        
        # 먼저 출력값이 0인 경우 설정
        # 1. 입력 길이가 0인 경우
        # 2. 첫문자에 바로 알파벳이 오는 경우
        # 3. 첫문자에 숫자가 안오고 '.'이 오는 경우
        # 4. 입력이 '+'이거나 '-'인 경우
        # 5. 입력 길이가 2 이상일 때 처음에 연속으로 '+-'나 '-+'가 오는 경우
        if len(s)==0 or s[0].isalpha()==True or s[0] == '.':
            return 0
        
        if s == "+" or s == "-":
            return 0
        
        if len(s) >= 2:
            if (s[0] == '+' and s[1] == '-') or (s[1] == '+' and s[0] == '-'):
                return 0
        
        # 빈 문자열 생성시키고 처음에 부호가 있으면 부호 저장
        # 그 다음에 문자들이 숫자인지 판별하고 result 문자열에 저장
        # 만약 알파벳이 오면 for문 종료
        result=''
        if s[0] == '+' or s[0] == '-':
                result += s[0]
                    
        for i,c in enumerate(s):
            if (i==0) and ((c == '+') or (c == '-')):
                continue
                
            if c.isdigit():
                result += c
            else:
                break
        
        # result 결과 문자열이 앞에 부호가 있는 경우 부호를 고려하여 숫자 판별
        # 그리고 숫자인지 최종적으로 판별했으면 문자열을 정수형으로 변환
        if result.isdigit()==False:
            if (result[0]=='-' or result[0]=='+') and result[1:].isdigit() == True:
                result = int(result)
            else:
                return 0
        
        result = int(result)
        
        # 변환된 정수를 범위내에 존재 여부에 따라 최종 출력값 판별
        if result >= max_int:
            return max_int

        elif result <= min_int:
            return min_int

        else:
            return result
