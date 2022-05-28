class Solution:
  """
  Runtime: 32 ms, faster than 84.15% of Python3 online submissions for Decode String.
  """
  
  
    
    def decodeString(self, s: str) -> str:
        
        # stack을 사용할 건데, stack에서 pop하면 순서가 거꾸로 나와서
        # reverse해주는 코드를 작성
        
        def reverse_str(string):
            string = list(string)
            string.reverse()
            string = ''.join(string)
            return string
        
        
        alpha_stack = [] # 알파벳이 담길 스택
        decimal_stack = [] # 곱해질 수가 담길 스택
        count_stack = [] # 한자리 수 이상인 숫자가 들어오면 decimal stack에서 count_stack의 숫자만큼 pop할거임
        
        cnt = 0 # 숫자가 몇자리 수인지 파악하기 위한 cnt
        
        for i in s:
                
            if i == "]": # 만일 닫힌 괄호가 오면,
                
                temp = ''
                while alpha_stack:
                    
                    last = alpha_stack.pop() # 이제까지 쌓인 알파벳을 빼내는데
                    if last == "[": # 그게 열린 괄호면 멈추고
                        break
                    temp += last # 그게 아니라면 알파벳을 쭉 이어줄거임
                
                loop = count_stack.pop() # 만일 곱해지는 숫자가 2자리 이상이면
                mul = ''
                for j in range(loop):
                    mul += decimal_stack.pop() # decimal stack에서 pop을 그 수만큼 해줌.
                """
                  예를 들어, "100[leetcode]" 라면
                  decimal_stack = [1, 0, 0]
                  count_stack = [3]
                  이렇게 담겨있을 것이고, counter_stack에서의 수만큼 decimal_stack에서 pop하는 것
                  
                """
                mul = reverse_str(mul) # stack이니 반대로 순서를 바꿔 001 -> 100 으로 바꾸는 거.
                alpha_stack.append(temp*int(mul))
            
            elif i.isdigit(): # 숫자면 decimal_stack에 추가
                
                cnt += 1
                decimal_stack.append(i)
                
                
            else:
                
                if cnt != 0:
                    count_stack.append(cnt)
                cnt = 0
                
                alpha_stack.append(i)
                    
        answer = ''
        
        for i in alpha_stack:

            i = reverse_str(i)
            answer += i
            
        return answer
