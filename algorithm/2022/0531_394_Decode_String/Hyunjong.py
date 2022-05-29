# 아이디어 : 문자열을 순서대로 탐색하면서 stack에 순서대로 문자를 append한다.
#          : ]을 발견하면 문자를 decoding한다. 
#          : decoding을 할 때는 [ 문자가 나올 때 까지 문자를 저장하고 [ 문자가 나오면 (앞의 숫자 x 저장된 문자) 연산을 수행한다.

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        
        # 문자열 전체 탐색
        for search_str in s:
            # 만약 탐색중인 문자가 ]이면
            if search_str == ']':
                # 변수 초기화
                tmp_str = ''
                str_num =''
                while True:
                    # stack 내부값 처리
                    tmp = stack.pop()
                    # stack값이 [ 이면
                    if tmp == '[':
                        # 숫자를 추출
                        while stack:
                            tmp_num = stack.pop()
                            if tmp_num.isdigit():
                                str_num += tmp_num
                            else:
                                stack.append(tmp_num)
                                break
                        # 추출된 숫자와 추출된 string을 처리
                        tmp_str = int(str_num[::-1]) * tmp_str[::-1]
                        # 다시 스택에 넣어줌
                        for stack_str in tmp_str:
                            stack.append(stack_str)
                        break
                    
                    else:
                        tmp_str += tmp
            # 탐색중인 문자가 ]이 아니면
            else:
                stack.append(search_str)   
        result = ''.join(stack)
        return result
