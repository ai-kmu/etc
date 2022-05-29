class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = 0 
        string = ''
        
        # 스택에 여태 생성한 문자 저장하고 ] 나오면 스택에서 이전에 저장한 문자 꺼내와서
        # num 만큼 곱해주고 다돌면 최종 문장 출력
        for i in s:
            # i가 [ 이면 스택에 여태 저장한 string, num 추가
            if i == '[':
                stack.append(string)
                stack.append(num)
                # 추가후 초기화
                string = ''
                num = 0
                
            # i 가 ] 이면 스택에서 꺼냄
            elif i == ']':
                # 문장, 숫자 순으로 저장 했으니까 숫자, 문자 꺼냄
                num_after = stack.pop()
                prevstring = stack.pop()
                # 문장은 이전에 저장한 문장 + num*현재 문장
                string = prevstring + num_after*string
                
            # 숫자를 stack 에 넣기위해 체크
            elif i.isdigit():     
                # num 이 10 이상의 수가 나왔을때 측정하기 위해서 
                num = num*10 + int(i)
                
            # 문자가 나오면 현재문장에 더해주기
            else:
                string += i
               
        # 마지막 문장 리턴
        return string
