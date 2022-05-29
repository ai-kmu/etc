class Solution:
    def decodeString(self, s):
        # string -> list로 바꿔서 처리 
        str_list = list(s)
        
        stk = list()
        result = ''
        tmp_int = 0
        
        for i in range(len(str_list)):
            # 여는 괄호일 경우 스택에 튜플형태로 저장
            if str_list[i] == '[':
                stk.append((result, tmp_int))
                result = ''
                tmp_int = 0
                continue
            # 닫는 괄호일 경우 스택에서 값을 꺼내와 result에 더해준다
            elif str_list[i] == ']':
                string, value = stk.pop()
                result = string + value * result
                continue
            # int('문자열')을 하면 ValueError -> except문에서 처리   
            # int('정수')는 정상적으로 동작 
            try:
                if int(str_list[i]) >= 0 and int(str_list[i]) <= 9:
                    # 정수가 두자리수 이상일때 기존 값에 10을 곱해서 더해준다.
                    tmp_int = tmp_int * 10 + int(str_list[i])
            except:
                result += str_list[i]
                
        return result
