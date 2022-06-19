class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        answer = 0 # 최대값을 저장할 변수
        stack = [] # 스택으로 풀기 위해 스택 선언
        
        
        for index, h in enumerate(heights):
            
            if not stack: # 스택이 비어있다면 우선 추가해준다.
                stack.append([index, h])
            
            else:
                
                pos = index
                
                while stack and stack[-1][1] > h:
                  """
                  현재 높이 h보다 큰 값들을 스택에서 꺼내서, 이 현재 높이 h를 기준으로
                  사각형의 넓이를 구한다.
                  """
                    last = stack.pop()
                                        
                    rec = (index - last[0]) * last[1] # 넓이 구하는 곳
                    
                    answer = max(rec, answer) # 이전 값과 비교하여 큰 값을 정답값으로 사용
                    
                stack.append([pos,h]) # 현재의 위치를 기준으로 스택에 새로 저장.

                
        return answer
      
        # 테스트 케이스는 통과하나 그 예외들은 어떻게 풀지 모르겠음.
