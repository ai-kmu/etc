class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        answer = ''
        
        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
                
            else:
                tmp = []
                num = []
                
                # 알파벳의 경우
                c = stack.pop()
                # '[' 직전까지의 알파벳을 모두 tmp 배열의 0번 index에 넣어준다
                while stack and c != '[':
                    tmp.insert(0, c)
                    c = stack.pop()
                                
                # 숫자의 경우 (1의 자리수가 아닌 경우도 있기 때문에 while문으로 처리)
                while stack and stack[-1].isdigit():
                    n = stack.pop()
                    num.insert(0, n)
                
                # num 배열의 element를 합쳐서 하나의 숫자로 만들어준다
                num = ''.join(num)
                num = int(num)
                
                # tmp 배열을 num times 만큼 곱해주고 stack에 append
                tmp *= num
                for i in tmp:
                    stack.append(i)
                    
        answer = ''.join(stack)                
        return answer
