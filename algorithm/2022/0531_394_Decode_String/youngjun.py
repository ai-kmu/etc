class Solution:
    def decodeString(self, s: str) -> str:
            # 문자열 리스트, 숫자, 이들을 담을 빈 stack을 만들어 준다.
            words = []
            num = 0
            stack = []
            
            for ch in s:
                # 숫자의 경우, num에 저장한다.
                if ch.isdigit():
                    num = num * 10 + int(ch)
                # 문자열의 경우 'word'라는 리스트에 계속 저장한다
                elif ch.isalpha():
                    words.append(ch)
                # 열린 괄호가 나오면 num과 word를 차례로 저장한다. 이때 만약 word가 없을 경우, 빈 리스트를 저장하게 된다.
                elif ch == '[':
                    stack.append(num)
                    stack.append(words)
                    # stack에 저장 후 word와 num을 초기화시킨다.
                    words = []
                    num = 0
                # 닫힌 괄호가 나오면 word와 num을 차례로 pop 해준 다음, 괄호 속 word(word 리스트에 있는 문자열)을 pop된 num과 곱해주고, pop된 word와 더해준다.
                elif ch == ']':
                    popped_words = stack.pop()
                    popped_num = stack.pop()
                    words = popped_words + (popped_num * words)
            
            answer = ""
            for word in words:
                answer += word
                
            return answer
