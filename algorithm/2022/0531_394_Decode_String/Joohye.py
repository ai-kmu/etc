class Solution:
    def decodeString(self, s: str) -> str:
        # num을 담을 stack, string을 담을 stack 선언
        num_stack = [] 
        st_stack = []
        # 정답값, 곱할 수 담을 곳 선언
        answer = ''
        num = ''
        # s탐색, s안에는 string값과 num값이 섞여있음.
        for st_or_num in s:
            # digit(곱할 수)이면,
            if st_or_num.isdigit():
                num += st_or_num
            # alpha(문자)라면,
            elif st_or_num.isalpha():
                answer += st_or_num
            # 여는 대괄호([)를 만나면, stack에 추가
            elif st_or_num == '[':
                num_stack.append(answer)
                st_stack.append(int(num))
                #stack에 추가한 값은 초기화
                answer = ''
                num = ''
            # 닫는 대괄호(])를 만나는 경우
            else:
                answer = num_stack.pop() + answer * st_stack.pop()
        return answer    
